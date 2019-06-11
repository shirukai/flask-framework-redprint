FROM python:3
ARG SERVER_PORT=18666
MAINTAINER shirukai "shirukai@hollysys.net"

# set work dir
WORKDIR flask-framework-redprint

# copy server files
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

# expose server port
EXPOSE ${SERVER_PORT}

# set time zone
ENV TZ Asia/Shanghai
# start flask service when the container starts
CMD uwsgi uwsgi.ini