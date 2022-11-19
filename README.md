
# Mobile Image Generator

## General Info
This is an application that was built during Southern Utah's Codecamp ( a 24 hour codeathon ) and uses Stable Diffusion as the machine learning model for the image generation. There are 2 main parts to this project, the front-end written in Ionic with Vue.js and the back-end written in Python.
The reason Python was used in the back-end was so that we could load the initial model into memory and keep it there, decreasing the average time to generate a single image from ~30 seconds to ~6 seconds, making it a lot more usable for a web application

## Toolstack
* [Python](https://www.python.org/)
* [Ionic](https://ionicframework.com/)

# Build Instructions

## Python
Inside of `server.py` and `stableDiffusion2.py` changes might need to be made where the strings `/opt/stableDiffusion` and `http://coder.binary141.com/pics` are used to your own custom settings.


### `/opt/stableDiffusion`
---
This is the location where the images should be saved on disk and accessible by some sort of software that can serve these images. We used Apache web server for this purpose.

### `http://coder.binary141.com/pics`
---
This is the url of the Apache web server so images can be sent down to the front end.

## Ionic
Inside of the `mobile-photo-frontend/src/views/Tab*.js` files the url inside of the fetch requests will need to be modified to your custom settings. `http://code.binary141.com:6969` is the url and port where the python server is listening for requests and can serve content from.

