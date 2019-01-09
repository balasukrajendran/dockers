FROM selenium/standalone-chrome
RUN sudo apt-get update && sudo apt-get install -y python python-pip
RUN sudo pip install selenium

ENV name="bala"

RUN  mkdir -p ~/app
WORKDIR  ~/app

COPY first.py .

RUN find ~/ -name python
RUN find ~/ -name chrome
#CMD ["sh", "-c", "echo $name"]

CMD ["python", "first.py"]