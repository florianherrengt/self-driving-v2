FROM resin/rpi-raspbian:wheezy

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
RUN ln -s /usr/bin/pip-3.2 /usr/bin/pip3
