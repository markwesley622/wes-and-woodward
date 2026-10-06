#!/usr/bin/env python3
"""Local receiver for EliteProspects pulls made from Mark's logged-in Chrome.

The browser (claude-in-chrome, Browser 2) runs a small worker loop on an EP tab that asks this
server for work, fetches each EP page in-page with the session cookies, extracts the embedded
__NEXT_DATA__ payload and POSTs the compact result back here. Nothing on this side touches EP.

    python3 pipeline/ep_receiver.py            # serves on 127.0.0.1:8765
    python3 pipeline/ep_receiver.py enqueue <type> <key> <url> [...]   # add work
    python3 pipeline/ep_receiver.py status

Queue file: data/raw/ep/queue.json (list of {type,key,url}); results land in
data/raw/ep/<type>/<key>.json; failures in data/raw/ep/errors.jsonl.
"""
import json, sys, threading, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EP = ROOT / "data" / "raw" / "ep"
QUEUE = EP / "queue.json"
LOCK = threading.Lock()
PORT = 8765


def load_queue():
    return json.load(QUEUE.open()) if QUEUE.exists() else []


def save_queue(q):
    EP.mkdir(parents=True, exist_ok=True)
    tmp = QUEUE.with_suffix(".tmp")
    tmp.write_text(json.dumps(q))
    tmp.replace(QUEUE)


def done_path(t):
    return EP / t["type"] / f"{t['key']}.json"


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body):
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_OPTIONS(self):
        self._send(200, {})

    def do_GET(self):
        if self.path.startswith("/next"):
            n = 3
            if "n=" in self.path:
                n = int(self.path.split("n=")[1].split("&")[0])
            with LOCK:
                q = load_queue()
                out, rest = [], []
                for t in q:
                    if len(out) < n and not t.get("leased"):
                        t = dict(t); t["leased"] = time.time(); out.append(t)
                    elif t.get("leased") and time.time() - t["leased"] > 180:   # stale lease: hand it out again
                        t = dict(t); t.pop("leased"); rest.append(t); continue
                    rest.append(t)
                save_queue(rest)
            self._send(200, {"tasks": [{k: v for k, v in t.items() if k != "leased"} for t in out]})
        elif self.path.startswith("/status"):
            q = load_queue()
            self._send(200, {"queued": len(q), "leased": sum(1 for t in q if t.get("leased")),
                             "done": {d.name: len(list(d.glob("*.json"))) for d in EP.iterdir() if d.is_dir()}})
        else:
            self._send(404, {"error": "no"})

    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0)
        body = json.loads(self.rfile.read(n) or b"{}")
        if self.path == "/save":
            t = body["task"]
            p = done_path(t); p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(body["data"]))
            with LOCK:
                save_queue([x for x in load_queue() if not (x["type"] == t["type"] and x["key"] == t["key"])])
            self._send(200, {"ok": True})
        elif self.path == "/error":
            t = body["task"]
            EP.mkdir(parents=True, exist_ok=True)
            with (EP / "errors.jsonl").open("a") as f:
                f.write(json.dumps({**t, "error": body.get("error"), "status": body.get("status"), "at": time.time()}) + "\n")
            with LOCK:
                q = load_queue()
                for x in q:
                    if x["type"] == t["type"] and x["key"] == t["key"]:
                        x.pop("leased", None); x["tries"] = x.get("tries", 0) + 1
                        if x["tries"] >= 3: x["dead"] = True
                save_queue([x for x in q if not x.get("dead")])
            self._send(200, {"ok": True})
        elif self.path == "/enqueue":
            with LOCK:
                q = load_queue(); have = {(t["type"], t["key"]) for t in q}
                added = 0
                for t in body["tasks"]:
                    if (t["type"], t["key"]) in have or (done_path(t).exists() and not t.get("force")): continue
                    q.append({"type": t["type"], "key": t["key"], "url": t["url"]}); have.add((t["type"], t["key"])); added += 1
                save_queue(q)
            self._send(200, {"added": added, "queued": len(q)})
        else:
            self._send(404, {"error": "no"})


def enqueue(tasks):
    with LOCK:
        q = load_queue(); have = {(t["type"], t["key"]) for t in q}
        for t in tasks:
            if (t["type"], t["key"]) in have or done_path(t).exists(): continue
            q.append(t); have.add((t["type"], t["key"]))
        save_queue(q)
    return len(q)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "enqueue":
        a = sys.argv[2:]
        tasks = [{"type": a[i], "key": a[i + 1], "url": a[i + 2]} for i in range(0, len(a), 3)]
        print("queued:", enqueue(tasks))
    elif len(sys.argv) > 1 and sys.argv[1] == "status":
        q = load_queue(); print(json.dumps({"queued": len(q), "leased": sum(1 for t in q if t.get("leased"))}))
    else:
        print(f"ep_receiver on 127.0.0.1:{PORT}, queue at {QUEUE}")
        ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
