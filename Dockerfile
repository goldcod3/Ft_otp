FROM debian:latest

# Install Dependencies
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install sudo zip vim -y
RUN apt-get install oathtool python3 python3-pip -y
RUN pip install cryptography

# User target configuration
RUN useradd -m dev
RUN usermod -s /bin/bash dev
RUN usermod -aG sudo dev
RUN echo "dev:42madrid" | chpasswd

# Volume directory
RUN mkdir -p /home/dev/src
RUN mkdir -p /home/dev/out

USER dev

ENTRYPOINT bash
