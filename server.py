# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import time
import os
import json

hostName = "0.0.0.0"
# hostName = "localhost"
serverPort = 6969

STABLE_DIFFUSION = True

if STABLE_DIFFUSION:
    import stableDiffusion2
    imggen = stableDiffusion2.theAlgo()


class MyServer(BaseHTTPRequestHandler):
    protocol_version: str = 'HTTP/1.1'
    def do_GET(self):
        try:
            if "ListImages" in self.path.split("/")[1]:
                print("They are here!")
                files = os.listdir("/opt/stableDiffusion")
                arr = []
                for file in files:
                    if file.endswith(".png"):
                        arr.append(file)
                # print("files: ", files)

                response = b'{"images": ' + bytes('"' + ','.join(arr) + '"', 'utf-8') + b'}'
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header("Content-Length", len(response))
                self.send_header("Content-type", "application/json")
                self.end_headers()



                self.wfile.write(response)
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
        except Exception as e:
            print("The error was: \n", e)
            self.send_error(500,"there was an error")

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    path = imggen.generate("warmup")
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
        print('hi')
        print(webServer.client_address())
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
