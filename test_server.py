# #!/usr/bin/env python3
#
# # It's python3 -m http.server PORT for a CORS world
#
# from http.server import HTTPServer, SimpleHTTPRequestHandler
# import sys
#
# class CORSRequestHandler(SimpleHTTPRequestHandler):
#     def end_headers(self):
#         self.send_header('Access-Control-Allow-Origin', '*')
#         self.send_header('Access-Control-Allow-Methods', '*')
#         self.send_header('Access-Control-Allow-Headers', '*')
#         self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
#         return super(CORSRequestHandler, self).end_headers()
#
#     def do_OPTIONS(self):
#         self.send_response(200)
#         self.end_headers()
#
#     def do_GET(self):
#         givenPath = self.path.split("/")[2]
#         print("givenPath: ", givenPath)
#         # decodedURL = urllib.parse.unquote(givenPath)
#         # imgLocation= imggen.generate(decodedURL)
#         # imgLocation = "Hello"
#         self.send_header("Content-type", "text/html")
#         self.send_header('Access-Control-Allow-Origin', '*')
#         self.end_headers()
#         self.send_response(200)
#         # self.wfile.write(str(imgLocation).encode())
#         # print(imgLocation, '\n\n')
#
# host = '0.0.0.0'
# port = 6970
#
# print("Listening on {}:{}".format(host, port))
# httpd = HTTPServer((host, port), CORSRequestHandler)
# httpd.serve_forever()
#!/usr/bin/env python3

# encoding: utf-8

"""Use instead of `python3 -m http.server` when you need CORS"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json


class CORSRequestHandler(SimpleHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(CORSRequestHandler, self).end_headers()

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("Hello".encode())
        # self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))


    def do_HEAD(self):
        self._set_headers()
    #     # givenPath = self.path.split("/")[2]
    #     # print("givenPath: ", givenPath)
    #     # decodedURL = urllib.parse.unquote(givenPath)
    #     # imgLocation= imggen.generate(decodedURL)
    #     # imgLocation = "Hello"
    #     self.send_header("Content-type", "text/html")
    #     self.send_header('Access-Control-Allow-Origin', '*')
    #     self.send_header('Content-Length', len("Hello"))
    #     self.end_headers()
    #     self.wfile.write("Hello".encode())
    #     self.send_response(200)

    #     # print(imgLocation, '\n\n')


httpd = HTTPServer(('0.0.0.0', 6970), CORSRequestHandler)
httpd.serve_forever()
