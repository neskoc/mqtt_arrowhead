#!/bin/bash

AH_root_path=/etc/arrowhead/
new_certs_root_path=~/Dropbox/iot/project/code/cert-generation/private/

# stop all arrowhead services
sudo systemctl stop arrowhead-authorization
sudo systemctl stop arrowhead-choreographer
sudo systemctl stop arrowhead-event-handler
sudo systemctl stop arrowhead-gatekeeper
sudo systemctl stop arrowhead-gateway
sudo systemctl stop arrowhead-orchestrator
sudo systemctl stop arrowhead-serviceregistry

./replace-passwords.bash

# first backup the old p12 cert-files
sudo find ${AH_root_path}  -name '*.p12' -exec bash -c 'mv $0 ${0/\.p12/\.p12\.old}' {} \;

# copy new certificates from the place where those are stored (new_certs_root_path)
sudo cp ${new_certs_root_path}/cloud-root/crypto/* ${AH_root_path}

# new root certificate is using the name "root" instead of "master" which is default
sudo cp ${new_certs_root_path}/cloud-root/crypto/* ${AH_root_path}

sudo cp ${new_certs_root_path}cloud-data-producer/crypto/truststore.p12 ${AH_root_path}
sudo cp ${new_certs_root_path}cloud-data-producer/crypto/mqtt_cloud-producer.* ${AH_root_path}clouds/

sudo cp ${new_certs_root_path}cloud-data-producer/crypto/authorization* ${AH_root_path}systems/authorization/
sudo cp ${new_certs_root_path}cloud-data-producer/crypto/event_handler* ${AH_root_path}systems/event_handler/
sudo cp ${new_certs_root_path}cloud-data-producer/crypto/gatekeeper* ${AH_root_path}systems/gatekeeper/
sudo cp ${new_certs_root_path}cloud-data-producer/crypto/gateway* ${AH_root_path}systems/gateway/
sudo cp ${new_certs_root_path}cloud-data-producer/crypto/orchestrator* ${AH_root_path}systems/orchestrator/
sudo cp ${new_certs_root_path}cloud-data-producer/crypto/service_registry* ${AH_root_path}systems/service_registry/
sudo cp ${new_certs_root_path}cloud-data-producer/crypto/sysop* ${AH_root_path}systems/sysop/

# cert scripts are using different naming convention "contract_proxy" is used instead of "choreographer"
sudo cp ${new_certs_root_path}cloud-data-producer/crypto/contract_proxy.p12 ${AH_root_path}systems/choreographer/choreographer.p12
sudo cp ${new_certs_root_path}cloud-data-producer/crypto/contract_proxy.pub ${AH_root_path}systems/choreographer/choreographer.pub

# change group owner to arrowhead
sudo chown :arrowhead ${AH_root_path}systems/*/*
sudo chown :arrowhead ${AH_root_path}*.crt
sudo chown :arrowhead ${AH_root_path}*.p12
sudo chown :arrowhead ${AH_root_path}clouds/*

# remove read permission for other
sudo find ${AH_root_path} -name '*.crt' -exec chmod o-r {} \;
sudo find ${AH_root_path} -name '*.p12' -exec chmod o-r {} \;

# start all arrowhead services                                                        
sudo systemctl start arrowhead-serviceregistry
sudo systemctl start arrowhead-authorization
sudo systemctl start arrowhead-choreographer
sudo systemctl start arrowhead-event-handler
sudo systemctl start arrowhead-gatekeeper
sudo systemctl start arrowhead-gateway
sudo systemctl start arrowhead-orchestrator
