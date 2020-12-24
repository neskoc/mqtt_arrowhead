# Installation and configuration

## Docker

```bash
sudo apt update
sudo apt upgrade
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common

cd ~/Downloads

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt update

sudo apt-get install docker-ce docker-ce-cli containerd.io
```

### Docker Compose

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

sudo curl -L https://raw.githubusercontent.com/docker/compose/1.27.4/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose
```

- bash completion
    `sudo curl -L https://raw.githubusercontent.com/docker/compose/1.27.4/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose`

## [Arrowhead Managemnt Tools](https://github.com/arrowhead-tools/mgmt-tool-js)

Installation as docker image
First pull the image from registry
'sudo docker pull svetlint/management-tool`

... then run it with `docker run` command

example:
`docker run -it -p 3000:5000 \
--name management-tool \
-e ARROWHEAD_SR_URL=http://arrowhead.tmit.bme.hu:8342 \
-e ARROWHEAD_ORCH_URL=http://arrowhead.tmit.bme.hu:8340 \
-e ARROWHEAD_GK_URL=http://arrowhead.tmit.bme.hu:8348 \
svetlint/management-tool`

`docker run -it -p 3000:5000 \
--name management-tool \
-e ARROWHEAD_SR_URL=localhost:8342 \
-e ARROWHEAD_ORCH_URL=localhost:8340 \
-e ARROWHEAD_GK_URL=localhost:8348 \
svetlint/management-tool
`
![Post installation/build](img/management-tool-post-install.png "Profilbild")
After installation docker container can be run with the command:
`docker start management-tool`

Web interface on host is available as: `http://172.17.0.2:5000`

## Eclipse-Mosquitto

### Install and Configure

Mosquitto is going to be installed on Raspberry Pi 3

1. Install docker if not already installed


    [Difference between up, run and start](https://docs.docker.com/compose/faq/#whats-the-difference-between-up-run-and-start)

    Typically, you want docker-compose up. Use up to start or restart all the services defined in a docker-compose.yml. In the default “attached” mode, you see all the logs from all the containers. In “detached” mode (-d), Compose exits after starting the containers, but the containers continue to run in the background.

    Use `docker-compose up` to start or restart all the services defined in a __docker-compose.yml__. In the default “attached” mode, you see all the logs from all the containers. In “detached” mode (__-d__), Compose exits after starting the containers, but the containers continue to run in the background.

    The `docker-compose run` command is for running “one-off” or “adhoc” tasks. It requires the service name you want to run and only starts containers for services that the running service depends on. Use run to run tests or perform an administrative task such as removing or adding data to a data volume container. The run command acts like docker run __-ti__ in that it opens an interactive terminal to the container and returns an exit status matching the exit status of the process in the container.

    Basicaly use `docker-compose run` to execute commands against a running service, and `docker-compose up` to spawn a new service
2. Pull mosquitto docker image see [Docker official images](https://registry.hub.docker.com/_/eclipse-mosquitto)
    `docker pull eclipse-mosquitto`
3. Run
    - interactivly
    `docker run -it -p 1883:1883 -p 9001:9001  eclipse-mosquitto`
    - as deamon
    `docker run -d -p 1883:1883 -p 9001:9001  eclipse-mosquitto`

### Configure firewall (ufw)

Add following rules
```bash
# client port: 1883 (defautl MQTT port)
sudo ufw allow from 192.168.1.0/24 to any port 1883

# client TLS port: 8883 (default port for MQTT over TLS)
sudo ufw allow from 192.168.1.0/24 to any port 8883

# admin port: 9001
sudo ufw allow from 192.168.1.0/24 to any port 9001
```