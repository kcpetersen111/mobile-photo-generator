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
        self.send_header("Connection", "close")
        # self.send_header("keep-alive", "timeout=1, max=10")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.wfile.write(response)
        self.end_headers()


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")