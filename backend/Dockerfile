FROM ubuntu:22.04
CMD nvidia-smi

ENV DEBIAN_FRONTEND=noninteractive

COPY requirements.txt ./

RUN apt-get update
RUN apt-get install -y python3 python3-pip nvidia-cudnn wget

# These next few lines are to be able to add the libcudnn packages to get the GPU to be detected by the container
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
RUN mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/3bf863cc.pub
RUN apt-get install -y software-properties-common
RUN add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /"


RUN apt-get update
RUN apt-get install libcudnn8
# RUN apt-get install libcudnn8-dev
RUN pip install -r requirements.txt
# RUN apt-get update && apt-get upgrade -y

COPY server.py .
COPY stableDiffusion2.py .

EXPOSE 6969

CMD ["python3", "./server.py"]
