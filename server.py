# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
# import stableDiffusion2
import urllib.parse


hostName = "0.0.0.0"
# hostName = "localhost"
serverPort = 6969
# imggen = stableDiffusion2.theAlgo()

class MyServer(BaseHTTPRequestHandler):
    protocol_version: str = 'HTTP/1.1'
    def do_GET(self):
        stuff = self.path.split("/")[2]
        decodedURL = urllib.parse.unquote(stuff)
        response = b'{data: ' + bytes(decodedURL, 'utf-8') + b'}'
        # stuff = imggen.generate(decodedURL)
        print(stuff)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Content-Length", len(response))
        self.end_headers()
        self.wfile.write(response)
        

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")