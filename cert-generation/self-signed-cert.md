# Generating self-signed certificate for Eclipse Mosquitto

```bash
openssl genrsa -des3 -out mosquitto-ca.key 2048

openssl req -new -x509 -days 3650 -key mosquitto-ca.key -out mosquitto-ca.crt
# Enter pass phrase for mosquitto-ca.key:
# Country Name (2 letter code) [AU]:SE
# State or Province Name (full name) [Some-State]:Stockholm
# Locality Name (eg, city) []:Stockholm
# Organization Name (eg, company) [Internet Widgits Pty Ltd]:CAmaster
# Organizational Unit Name (eg, section) []:umu
# Common Name (e.g. server FQDN or YOUR name) []:mqtt
# Email Address []:email@mail.com

openssl genrsa -out mqtt-server.key 2048
```

```bash
openssl req -new -out mqtt-server.csr -key mqtt-server.key

# Country Name (2 letter code) [AU]:SE
# State or Province Name (full name) [Some-State]:Stockholm
# Locality Name (eg, city) []:Stockholm
# Organization Name (eg, company) [Internet Widgits Pty Ltd]:Server-cert
# Organizational Unit Name (eg, section) []:umu
# Common Name (e.g. server FQDN or YOUR name) []:127.0.0.1
# Email Address []:email@mail.com

# Please enter the following 'extra' attributes to be sent with your certificate request
# A challenge password []:
# An optional company name []:
```

```bash
openssl x509 -req -in mqtt-server.csr -CA mosquitto-ca.crt -CAkey mosquitto-ca.key -CAcreateserial -out mqtt-server.crt -days 3650
# Signature ok
# subject=C = SE, ST = Stockholm, L = Stockholm, O = Server-cert, OU = umu, CN = 127.0.0.1, emailAddress = email@mail.com
# Getting CA Private Key
# Enter pass phrase for mosquitto-ca.key:
```
