#!/usr/bin/python

import sys, subprocess
import BaseHTTPServer
import SocketServer

PORT = 8080

if len(sys.argv) < 3:
    exit("Error: have to provide destination file and paths to whitelist and block scripts")

WL_TXT = sys.argv[1]
WL_SH = sys.argv[2]
BLOCK_SH = sys.argv[3]

if len(sys.argv) > 4:
    PORT = int(sys.argv[4])

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
        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0
        data = self.rfile.read(length)

        print("\n----- Handling Request ----->\n")
        print(request_path)

        print(request_headers)
        if request_path == "/whitelist.txt":
            print("New whitelist: \n", data)
            with open(WL_TXT, "w") as f:
                f.write(data)
            subprocess.call(['sudo', WL_SH])

        if request_path == "/block":
            print("Blocking: ", data)
            subprocess.call(['sudo', BLOCK_SH, data])


        print("<----- Request Finished -----\n")

        self.send_response(200)



print "Serving at port", PORT

httpd = SocketServer.TCPServer(("", PORT), WLHandler)
httpd.serve_forever()
