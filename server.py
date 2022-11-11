# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import stableDiffusion2
import urllib.parse


hostName = "0.0.0.0"
# hostName = "localhost"
serverPort = 6969
imggen = stableDiffusion2.theAlgo()

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        givenPath = self.path.split("/")[2]
        decodedURL = urllib.parse.unquote(givenPath)
        imgLocation= imggen.generate(decodedURL)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self._response_body( {"filePath":imgLocation})
        print(imgLocation, '\n\n')


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")