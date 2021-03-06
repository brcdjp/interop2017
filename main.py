#!/usr/bin/env python

from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
from threading import Thread
import goku

json_file = '/home/pi/interop2017/result.json'

class HttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        file_content = self.rfile.read(content_length)

        if file_content == "led":
            goku.led(file_content)
        elif file_content == "voice":
            goku.voice(file_content)
        elif file_content == "effect":
            goku.voice('effect')
        elif file_content == "goku_vote":
            goku.vote('goku')
        elif file_content == "freeza_vote":
            goku.vote('freeza')
        else :
            print(file_content)
            print("else")
        self.send_response(200)
        return

    def do_GET(self):
        f = open(json_file)
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(f.read())
        f.close()
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """ """  

if __name__=="__main__":
    goku.init()
    httpd = ThreadedHTTPServer(("", 80),HttpHandler)
    httpd.serve_forever()
