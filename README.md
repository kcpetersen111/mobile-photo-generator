
# Mobile Image Generator

## General Info
This is an application that was built during Southern Utah's Codecamp ( a 24 hour codeathon ) and uses Stable Diffusion as the machine learning model for the image generation. There are 2 main parts to this project, the front-end written in Ionic with Vue.js and the back-end written in Python.
The reason Python was used in the back-end was so that we could load the initial model into memory and keep it there, decreasing the average time to generate a single image from ~30 seconds to ~6 seconds, making it a lot more usable for a web application

## Toolstack
* [Python](https://www.python.org/)
* [Ionic](https://ionicframework.com/)

## Build Instructions
This repo makes use of Dockerfiles to create docker containers, make note of the docker bind mount on the back-end portion. This is to allow the server to save files to the host machine, as this also makes use of Apache web server to get the images back to the client. The steps to build this portion of the repository are:

### Back-end
```
git clone https://github.com/kcpetersen111/mobile-photo-generator.git
git switch docker
cd backend
docker build -t mobileImageGenerator-backend .
docker run --gpus all -dp 6969:6969 -v /opt/stableDiffusion:/opt/stableDiffusion mobileImageGenerator-backend
```

### Front-end
```
git clone https://github.com/kcpetersen111/mobile-photo-generator.git
git switch docker
cd frontend
docker build -t mobileImageGenerator-frontend .
docker run -dp 8080:8080 test-front
```

---
Inside of the Dockerfile for the back-end there are the 2 lines:
```
ENV remoteImageURL="http://coder.binary141.com/pics"
ENV imageSaveLocation="/opt/stableDiffusion"
```
These are made use in the python files, and are injected as environment variables.

### `imageSaveLocation`
This declares where the images are saved to as a PNG file on the disk. This was made accessible to all users with all permissions on my system with `chmod 777 /opt/stableDiffusion` as I didn't want to deal with any other issues and was a quick fix, but isn't the recommended folder permissions.

### `remoteImageURL`
This is used to formulate the full URL that the front-end uses to grab the images from. Apache2 was used as a way to be able to view the images from the front-end, so the url pointed to the domain that hosted these images

