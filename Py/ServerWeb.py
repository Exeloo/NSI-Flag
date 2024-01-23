import io

from Flag import *
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys
import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header("Cache-Control", "max-age=31536000")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Accept, Content-Type')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('X-Content-Type-Options', 'no-sniff')
        
        
        if self.path.replace("/", "") == "Flags" :
            self.send_header("Content-type", "text/http")
            self.end_headers()
            self.wfile.write(bytes(getFlagList(), "utf-8"))
            return

        self.send_header("Content-type", "image/x-icon")
        self.end_headers()

        if self.path.replace("/", "") == "favicon.ico" or self.path.replace("/", "") == "icon" :
            img = getIcon()

        else :
            path = self.path.replace('/', '')
            path = path.replace('%C3%A9', 'é')
            path = path.replace('%C3%A8', 'è')
            path = path.replace('%C3%B4', 'ô')
            path = path.replace('%C3%AF', 'ï')
            img = getFlag(path)
            if not img :
                img = getDefaultFlag() #Error

        with io.BytesIO() as output:
            img.save(output, format="JPEG")
            contents = output.getvalue()
        self.wfile.write(contents)

        return

handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

print("Le serveur est lancé sur le port", PORT)
my_server.serve_forever()
