# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import stableDiffusion2
import urllib.parse


hostName = "0.0.0.0"
# hostName = "localhost"
serverPort = 6969
imggen = stableDiffusion2.theAlgo()

class MyServer(BaseHTTPRequestHandler):
    protocol_version: str = 'HTTP/1.1'
    def do_GET(self):
        prompt = self.path.split("/")[2]
        decodedURL = urllib.parse.unquote(prompt)
        
        path = imggen.generate(decodedURL)
        print(path)

        response = b'{"data": ' + bytes('"'+path+'"', 'utf-8') + b'}'
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Content-Length", len(response))
        self.send_header("Connection", "keep-alive")
        self.send_header("keep-alive", "timeout=15, max=30")
        self.send_header('Access-Control-Allow-Origin', '*')
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