from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os, sys
class H(BaseHTTPRequestHandler):
    def do_POST(self):
        n=int(self.headers.get('Content-Length',0)); body=self.rfile.read(n)
        name=os.path.basename(self.path.strip('/')) or 'out.csv'
        open(name,'wb').write(body); print('saved',name,len(body),flush=True)
        self.send_response(200); self.send_header('Access-Control-Allow-Origin','*'); self.end_headers()
    def do_OPTIONS(self):
        self.send_response(200); self.send_header('Access-Control-Allow-Origin','*'); self.send_header('Access-Control-Allow-Headers','*'); self.end_headers()
    def log_message(self,*a): pass
ThreadingHTTPServer(('127.0.0.1',8765),H).serve_forever()
