FROM ubuntu:latest

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# Z kmenové složky do workdir
COPY . .

