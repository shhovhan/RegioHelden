# User Administration with google account
Simple Django application to manage (CRUD) users and their bank account data (IBAN) using Google account for authentication.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project.
### Prerequisites

What additional tools you need to install and build the software:
* Docker Engine
* Docker Compose
### Installing

Install Docker Engine on Ubuntu
* sudo apt-get update
* sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
* sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
* sudo apt-get update
* apt-cache policy docker-engine
* sudo apt-get install -y docker-engine
* sudo systemctl status docker

It should return something like this:
```
docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: active (running) since Sun 2018-11-11 20:09:05 +04; 9s ago
     Docs: https://docs.docker.com
 Main PID: 5528 (dockerd)
    Tasks: 24
   CGroup: /system.slice/docker.service
           ├─5528 /usr/bin/dockerd -H fd://
           └─5557 docker-containerd -l unix:///var/run/docker/libcontainerd/docker-containerd.sock --metrics-interval=0 --start-timeout 2m --s
 ```
Docker engine is ready. For more information and additional settings, please see: [Docker engine setup](https://docs.docker.com/install/#server)

Install Docker Compose on Ubuntu
* sudo apt-get install curl
* sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
* sudo chmod +x /usr/local/bin/docker-compose
* docker-compose --version

It should return something like this:
```
docker-compose version 1.23.1, build 1719ceb
```
For more information and additional settings, please see: [Docker Compose setup](https://docs.docker.com/compose/install/)

## Deployment

Clone or download the project. Go to the project directory and run the following commands to build the app
* sudo docker-compose build
* sudo docker-compose up
* open your browser and type: localhost:8000

Application is ready to use.

## Built With
* [Python 3+](https://docs.python.org/3/)
* [Django v2.1](https://docs.djangoproject.com/en/2.1/)
* [PostgreeSQL](https://www.postgresql.org/)
* [Django social-auth](https://python-social-auth-docs.readthedocs.io/en/latest/configuration/django.html)

### Testing
Application tested on Ubuntu 16.04+. If your Ubuntu version is < 16.04, then check repository for docker and use correct repository.

## Authors

Shushan Hovhannisyan
