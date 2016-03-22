#!/usr/bin/python

import sys
import BaseHTTPServer
import SocketServer

PORT = 8080

if len(sys.argv) < 2:
    exit("Error: have to provide destination file")

FILEPATH = sys.argv[1]

if len(sys.argv) > 2:
    PORT = int(sys.argv[2])

class WLHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head></head>")
        self.wfile.write("<body><p>The handler is working.</p>")
        self.wfile.write("<p>You accessed path: %s</p>" % s.path)
        self.wfile.write("</body></html>")
    def do_PUT(self):
        request_path = self.path

        print("\n----- Request Start ----->\n")
        print(request_path)

        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0
        whitelist = self.rfile.read(length)

        print(request_headers)
        with open(FILEPATH, "w") as f:
            f.write(whitelist)

        print(whitelist)
        print("<----- Request End -----\n")

        self.send_response(200)



print "Serving at port", PORT, "to", FILEPATH

httpd = SocketServer.TCPServer(("", PORT), WLHandler)
httpd.serve_forever()
