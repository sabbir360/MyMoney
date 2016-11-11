FROM ubuntu:14.04
# sabbir1cse/ubuntu-python-pip-supervisor
RUN apt-get update && apt-get install -y \ 
build-essential \
python \
python-dev \
libxml2-dev \
libxslt-dev \
libssl-dev \
zlib1g-dev \
libyaml-dev \
libffi-dev \
python-pip

RUN pip install --upgrade pip
RUN pip install supervisor
RUN apt-get install -y python3-pip

RUN mkdir /app && mkdir /home/ubuntu && mkdir /home/ubuntu/logs && mkdir /home/ubuntu/supervisorconf
ADD fake-django /app

RUN pip3 install -r /app/requirements.txt

COPY supervisord.conf /etc/supervisord.conf
# COPY webapp.conf  /etc/supervisor/conf.d/webapp.conf

WORKDIR /app

EXPOSE 8800 8801

# CMD ["uwsgi --http :80 --gevent 10  --module heart.wsgi"]

# ENTRYPOINT ["/usr/local/bin/uwsgi", "/etc/uwsgi.ini"]

# uwsgi --http :80 --gevent 10  --module heart.wsgi
CMD ["supervisord", "-n"]