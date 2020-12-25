# Installation and configuration

## AH local cloud

1. Download all necessary files if you don want to pull whole repository
```bash
# download all files
wget -c  https://github.com/arrowhead-f/core-java-spring-installers/raw/master/packages/arrowhead-core-common_4.1.3.deb
wget -c  https://github.com/arrowhead-f/core-java-spring-installers/raw/master/packages/arrowhead-authorization_4.1.3.deb
wget -c  https://github.com/arrowhead-f/core-java-spring-installers/raw/master/packages/arrowhead-choreographer_4.1.3.deb
wget -c  https://github.com/arrowhead-f/core-java-spring-installers/raw/master/packages/arrowhead-eventhandler_4.1.3.deb
wget -c  https://github.com/arrowhead-f/core-java-spring-installers/raw/master/packages/arrowhead-gatekeeper_4.1.3.deb
wget -c  https://github.com/arrowhead-f/core-java-spring-installers/raw/master/packages/arrowhead-gateway_4.1.3.deb
wget -c  https://github.com/arrowhead-f/core-java-spring-installers/raw/master/packages/arrowhead-orchestrator_4.1.3.deb
wget -c  https://github.com/arrowhead-f/core-java-spring-installers/raw/master/packages/arrowhead-serviceregistry_4.1.3.deb
```

Passwords chosen in the next/installatoins step are stored in `/var/cache/debconf/passwords.dat`
so if you forget ony you can find them there.
My recommendation is to use same the password everywhere in development environemnt or at least as long you are not comfortable with the system.
That will probalby save you some pulled or/and gray hair.

The other thing which is not clear is that you probalby will have to choose 

According to the instruction it is mandatory to currently use the following naming convention __my_cloud__.__my_company__.arrowhead.eu

When I looked on the ssl-certificate in my webbrowser I could see this certificate chain:

1. __arrowhead.eu__  
2. __mqtt_cloud.nesko.arrowhead.eu__  
3. __service_registry.mqtt_cloud.nesko.arrowhead.eu__

where __nesko__ is my alias and __mqtt_cloud__ is the name I've chosen for my local cloud.
I'm not realy sure what was the question where I answered with "nesko".


```bash
# assuming that files are downloaded in ~/Downloads
sudo apt install ~/Downloads/arrowhead-*.deb

```

### Removing AH cloud

If you by any reason need to remove/reinstall AH cloud use the following comman `sudo apt install ~/Downloads/arrowhead-*.deb`
I've so far done reinstall 2 times and I'm just preparing myself for the third one.
This time I'll be using same password for every part of the system (and make it simple for troubleshooting).

## certificates

Ignore [instruction](https://github.com/eclipse-arrowhead/core-java-spring/blob/master/documentation/certificates/import_sysop_certificate_linux.pdf) about installing test certificate in browser because that certificate is already expired.

After installing AH local cloude you can find __master.p12__-file at:  
`/etc/arrowhead/master.p12`

## TODO: Find out how passwords are generated!
I can't find the way to unlock it nor any other certificate generated during the cloud installation
I've tried both the default password __123456__,
the password I could find in .properties files (that password is called core-common during the installation) and
all the other passwords I've chosen during the installation (from now on I'll use the same password everywhere to make troubleshooting easier)

I've also used [scripts](https://github.com/eclipse-arrowhead/core-java-spring/tree/master/scripts/certificate_generation) to generate all certificates which are by default seved in ``

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
svetlint/management-tool`

After installing/building something similar to this will be shown:
![Post installation/build](img/management-tool-post-install.png "Managemnt tool")

After installation docker container can be run with the command:
`docker start management-tool`

Web interface on host is available as: `http://172.17.0.2:5000`  
![Mamagement-tool web interface](img/management-tool-web-interface.png "Mamagement-tool web interface")

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
