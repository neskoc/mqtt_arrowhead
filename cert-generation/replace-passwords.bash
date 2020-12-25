#!/bin/bash

sudo egrep -lRZ 'uJjCkMQB6ykDYAL3' --include='application.properties' /etc/arrowhead | sudo xargs -0 -l sed -i -e 's/uJjCkMQB6ykDYAL3/123456/g'
