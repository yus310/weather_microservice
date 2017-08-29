FROM ubuntu:12.04

RUN apt-get -y update --fix-missing
RUN apt-get install -y python-pip python-dev libev4 libev-dev gcc libxslt-dev libxml2-dev libffi-dev vim curl
RUN pip install --upgrade pip

RUN apt-get install -y python-numpy python-scipy
RUN pip install scikit-learn
RUN pip install flask-restful

ADD . /

EXPOSE 5000

CMD [ "python", "/api.py" ]