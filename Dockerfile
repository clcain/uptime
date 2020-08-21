FROM debian:buster-slim

RUN apt-get update && apt-get install python3 python3-pip -y && apt-get clean

WORKDIR /app
COPY /src ./

RUN pip3 install -r requirements.txt

ENTRYPOINT /usr/bin/env python3 -u main.py
