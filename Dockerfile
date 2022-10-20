FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y \
    python3 \
    python3-pip \
    git
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install \
    gradio \
    rembg
WORKDIR /
RUN git clone https://github.com/geeksloth/gradimio-rembg.git
WORKDIR /gradimio-rembg
CMD ["python3", "main.py"]