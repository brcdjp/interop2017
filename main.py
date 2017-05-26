#!/usr/bin/env python

import BaseHTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import goku

ipaddr = '172.24.197.208'

class HttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        file_content = self.rfile.read(content_length)

        if file_content == "goku":
            goku.led('goku')
        elif file_content == "freeza":
            goku.led('freeza')
        elif file_content == "goku_voice":
            goku.voice('goku')
        elif file_content == "freeza_voice":
            goku.voice('freeza')
        elif file_content == "sound_effect":
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
        f = open("/home/ubuntu/interop_demo/result.json")
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(f.read())
        f.close()
        return

if __name__=="__main__":
    httpd = BaseHTTPServer.HTTPServer((ipaddr, 80),HttpHandler)
    httpd.serve_forever()
