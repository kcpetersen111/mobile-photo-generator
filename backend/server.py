# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import time
import os
import json

remoteImageURL = os.environ['remoteImageURL']
imageSaveLocation = os.environ['imageSaveLocation']

hostName = "0.0.0.0"
serverPort = 6969

# Change this to false to just test some changes to the server faster than
# loading the model into memory
STABLE_DIFFUSION = True

if STABLE_DIFFUSION:
    import stableDiffusion2
    imggen = stableDiffusion2.theAlgo()

isWorking = False


class MyServer(BaseHTTPRequestHandler):
    protocol_version: str = 'HTTP/1.1'
    def do_GET(self):
        global isWorking

        if not isWorking:
            try:
                isWorking = True
                if "ListImages" in self.path.split("/")[1]:
                        files = os.listdir("%s" % imageSaveLocation)
                        arr = []
                        for file in files:
                            # Get all the png images
                            if file.endswith(".png"):
                                arr.append(remoteImageURL + file)

                        response = b'{"images": ' + bytes('"' + ','.join(arr) + '"', 'utf-8') + b'}'
                        self.send_response(200)
                        self.send_header('Access-Control-Allow-Origin', '*')
                        self.send_header("Content-Length", len(response))
                        self.send_header("Content-type", "application/json")
                        self.end_headers()

                        self.wfile.write(response)

                        # Force close the connection so that we can listen for
                        # requests from other clients
                        self.close_connection = True
                else:
                    prompt = self.path.split("/")[2]
                    decodedURL = urllib.parse.unquote(prompt)

                    if STABLE_DIFFUSION:
                        path = imggen.generate(decodedURL)
                        print(path)

                        response = b'{"data": ' + bytes('"'+path+'"', 'utf-8') + b'}'
                    else:
                        response = "Hello"

                    # print(webServer.client_address())
                    self.send_response(200)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.send_header("Content-Length", len(response))
                    self.send_header("Content-type", "application/json")
                    self.end_headers()

                    self.wfile.write(response)
                    self.close_connection = True
                    print(self.client_address)
                isWorking = False
            except Exception as e:
                print("The error was: \n", e)
                self.send_error(500,"there was an error")
        else:
            self.send_error(500,"there was an error")

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    if STABLE_DIFFUSION:
        # Run a warmup model initially to load everything it needs first to
        # make subsequent requests a little faster
        path = imggen.generate("warmup")
    print("Server started at http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
        print(webServer.client_address())
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
