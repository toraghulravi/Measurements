FROM python:3.7.3-stretch

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get install traceroute

RUN mkdir /work

WORKDIR /work

CMD ["python3", "main.py"]