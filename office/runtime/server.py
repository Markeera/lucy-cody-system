from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
import json,urllib.request,concurrent.futures,datetime
from urllib.parse import urlsplit
from pathlib import Path
ROOT=Path(__file__).parent
def probe(url):
 try:
  with urllib.request.urlopen(url,timeout=3) as r:
   return {"online":True,"data":json.load(r)}
 except Exception as e:return {"online":False,"error":str(e)}
def state():
 urls={"dashboard":"http://127.0.0.1:8765/api/health","queue":"http://127.0.0.1:8765/api/projects","task":"http://127.0.0.1:8765/api/task","engine":"http://127.0.0.1:8765/api/engine-readiness","voice":"http://127.0.0.1:3900/health","n8n":"http://127.0.0.1:5678/healthz"}
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: values=list(ex.map(probe,urls.values()))
 s=dict(zip(urls,values));s["checkedAt"]=datetime.datetime.now().astimezone().isoformat()
 # Do not expose task command or output logs.
 t=s["task"].get("data",{});s["task"]["data"]={k:t.get(k) for k in ("state","started","finished","exitCode")}
 q=s["queue"].get("data",{});s["queue"]["data"]={"projects":[{k:p.get(k) for k in ("id","status","archived","rejected","videoSeconds","humanReviewed")} for p in q.get("projects",[])]}
 return s
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  path=urlsplit(self.path).path
  if path=="/api/state": data=json.dumps(state(),ensure_ascii=False).encode();kind="application/json"
  elif path=="/approved-office.png":data=(ROOT/"approved-office.png").read_bytes();kind="image/png"
  elif path=="/":data=(ROOT/"index.html").read_bytes();kind="text/html; charset=utf-8"
  else:self.send_error(404);return
  self.send_response(200);self.send_header("Content-Type",kind);self.send_header("Cache-Control","no-store");self.send_header("Content-Length",str(len(data)));self.end_headers();self.wfile.write(data)
if __name__=="__main__":ThreadingHTTPServer(("127.0.0.1",8766),Handler).serve_forever()
