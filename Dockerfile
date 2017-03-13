FROM resin/rpi-raspbian:wheezy

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
RUN ln -s /usr/bin/pip-3.2 /usr/bin/pip3
RUN apt-get install python-picamera 
RUN apt-get -y install libraspberrypi-bin
RUN apt-get -y install python-rpi.gpio
RUN apt-get -y install python3-rpi.gpio
RUN pip3 install Flask