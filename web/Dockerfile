FROM alpine

# Initialize
RUN mkdir -p /data/web
WORKDIR /data/web/mydjango
COPY requirements.txt /data/web/

# Setup
RUN apk update
RUN apk upgrade
RUN apk add --no-cache --update python3 python3-dev postgresql-client postgresql-dev build-base gettext
RUN pip3 install --upgrade pip
RUN pip3 install -r ../requirements.txt

# Clean
RUN apk del -r python3-dev postgresql


# Prepare
COPY . /data/web/
RUN mkdir -p mydjango/static/admin
