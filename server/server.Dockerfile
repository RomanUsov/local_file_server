FROM tiangolo/uvicorn-gunicorn:python3.10 as server

RUN apt-get update -y && apt-get install -y \
    software-properties-common \
    python3-software-properties \
    build-essential \
    python3-dev

COPY requirements.txt /tmp

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

RUN apt-get update && apt install -y python3 python3-pip  && apt-get clean
RUN pip3 install --upgrade pip

RUN mkdir -p /src
WORKDIR /src

COPY config.py /src/config.py

WORKDIR /src/
