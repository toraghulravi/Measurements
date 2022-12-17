FROM python:3.7.3-stretch

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install scamper

RUN apt-get -y install dnsutils

COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN mkdir -p /work

COPY runner.sh /work/runner.sh

WORKDIR /work

CMD ["bash", "runner.sh"]