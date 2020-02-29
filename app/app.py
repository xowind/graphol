import io
import re
import subprocess
import urllib
from flask import Flask
from flask import send_file
from flask import request
from flask import Response
from HTMLParser import HTMLParser
app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello World from Flask"

def gvgen(src):
   if len(src) <= 0:
      msg =  "src is empty!"
      print msg
      return Response(msg, status=500, mimetype="image/png")
   else:
      png = None
      try:
         h = HTMLParser()
         src = h.unescape(src)
         src,_ = re.subn(r";\s*\n?", "\n", src)
         src,_ = re.subn(r"{\s*\n?", "{\n", src)
         src,_ = re.subn(r"}\s*\n?", "}\n", src)
         src,_ = re.subn(r"\n\s+", "\n", src)
         prog = "dot -Tpng -o /dev/stdout /dev/stdin 2>&1"
         if src.find("@startuml") > -1:
            prog = "java -Djava.awt.headless=true -jar /plantuml.jar -charset UTF-8 -p -tpng 2>&1"
         png = subprocess.check_output("echo '" + src + "'|" + prog, shell=True)
      except Exception, e:
         msg = "Failed: exec not exited with 0: " + str(e)
         print msg
         return Response(msg, status=500, mimetype="image/png")
      if png != None:
         return send_file(io.BytesIO(png),
                     attachment_filename='gvgen.png',
                     mimetype='image/png')

@app.route("/g")
def getg():
   src = urllib.unquote(request.query_string).decode('utf8')
   return gvgen(src)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=80)

