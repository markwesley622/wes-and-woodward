#!/usr/bin/env python3
"""Crop a player illustration to the site's art box and record it in pipeline/art_boxes.json.

Rule (Mark, 9/24): one 4:3 box, 1100 x 825, the face normalised to faceShare (21%) of the box height
with its centre at faceCentre (50%, 36%); areas outside the source are transparent. Bottom-contact
rule: if the box would extend below the figure, raise the face share until the box bottom sits on
the figure's last opaque row, so every illustration touches the bottom edge.

Faces come from macOS Vision (a tiny Swift tool compiled on the fly with xcrun).

Usage: python3 pipeline/crop_art.py <playerId> <source.png> [--face x,y,w,h]
Writes public/players/<id>-art.webp (q82) and <id>-art.png (128 colours), updates art_boxes.json.
"""
import json, pathlib, subprocess, sys, tempfile
import numpy as np
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
BOXES = ROOT / "pipeline" / "art_boxes.json"
SWIFT = '''
import Foundation
import Vision
import AppKit
let path = CommandLine.arguments[1]
guard let img = NSImage(contentsOfFile: path), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { print("[]"); exit(1) }
let req = VNDetectFaceRectanglesRequest()
try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
let W = CGFloat(cg.width), H = CGFloat(cg.height)
var out: [String] = []
for f in req.results ?? [] { let b = f.boundingBox; out.append(String(format: "[%.0f,%.0f,%.0f,%.0f]", b.origin.x * W, (1 - b.origin.y - b.height) * H, b.width * W, b.height * H)) }
print("[" + out.joined(separator: ",") + "]")
'''


def detect_face(src):
    d = pathlib.Path(tempfile.mkdtemp()); (d / "f.swift").write_text(SWIFT)
    subprocess.run(["xcrun", "swiftc", "-O", "-o", str(d / "f"), str(d / "f.swift")], check=True, capture_output=True)
    faces = json.loads(subprocess.run([str(d / "f"), str(src)], check=True, capture_output=True, text=True).stdout)
    if not faces: raise SystemExit("no face found; pass --face x,y,w,h")
    return max(faces, key=lambda f: f[2] * f[3])


def crop(pid, src, face=None):
    boxes = json.loads(BOXES.read_text())
    BW, BH = boxes["box"]; share = boxes["faceShare"]; fcx, fcy = boxes["faceCentre"]
    im = Image.open(src).convert("RGBA"); W, H = im.size
    alpha = np.array(im)[:, :, 3]; rows = np.where(alpha.max(1) > 8)[0]; fig_bottom = int(rows.max()) + 1
    x, y, w, h = face or detect_face(src)
    cx, cy = x + w / 2, y + h / 2
    def box_for(s):
        bh = h / s; bw = bh * BW / BH
        return cx - fcx * bw, cy - fcy * bh, bw, bh
    eff = share
    L, T, bw, bh = box_for(eff)
    if T + bh > fig_bottom:                       # bottom-contact rule: zoom until the box bottom meets the figure
        lo, hi = eff, 0.9
        for _ in range(60):
            mid = (lo + hi) / 2; L, T, bw, bh = box_for(mid)
            if T + bh > fig_bottom: lo = mid
            else: hi = mid
        eff = hi; L, T, bw, bh = box_for(eff)
    scale = BW / bw
    canvas = Image.new("RGBA", (BW, BH), (0, 0, 0, 0))
    resized = im.resize((round(W * scale), round(H * scale)), Image.LANCZOS)
    canvas.alpha_composite(resized, (round(-L * scale), round(-T * scale)))
    out_dir = ROOT / "public" / "players"
    canvas.save(out_dir / f"{pid}-art.webp", "WEBP", quality=82, method=6)
    canvas.quantize(colors=128, method=Image.Quantize.FASTOCTREE).save(out_dir / f"{pid}-art.png", optimize=True)
    a2 = np.array(canvas)[:, :, 3]; last = int(np.where(a2.max(1) > 8)[0].max()) + 1
    boxes["faces"][str(pid)] = {"name": boxes["faces"].get(str(pid), {}).get("name", ""), "source": str(src), "face": [int(x), int(y), int(w), int(h)], "effectiveShare": round(eff, 3)}
    BOXES.write_text(json.dumps(boxes, indent=1))
    print(f"{pid}: face {[int(x), int(y), int(w), int(h)]} share {eff:.3f} box {bw:.0f}x{bh:.0f} at ({L:.0f},{T:.0f}); last opaque row {last} of {BH}")
    return last


if __name__ == "__main__":
    pid = sys.argv[1]; src = pathlib.Path(sys.argv[2]).expanduser()
    face = [float(v) for v in sys.argv[sys.argv.index("--face") + 1].split(",")] if "--face" in sys.argv else None
    crop(pid, src, face)
