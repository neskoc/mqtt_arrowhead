## Adding Relay

A local cloud must know about the relay before using it, so you have to register the relay into the cloud's database. You can use the gatekeeper's Swagger interface to register the relay (or you can use the management tool if available):

    In a browser open the following address: https://<ip address of the testcloud1's gatekeeper>:8449
    Select the /gatekeeper/mgmt/relays POST request
    The input JSON object should be something like this:

```JSON
[
  {
    "address": "127.0.0.1",
    "exclusive": false,
    "port": 61617,
    "secure": true,
    "type": "GENERAL_RELAY"
  }
]
```

```bash
# cli command
curl -X POST "https://localhost:8449/gatekeeper/mgmt/relays" -H  "accept: application/json" -H  "Content-Type: application/json" -d "[  {    \"address\": \"127.0.0.1\",    \"exclusive\": false,    \"port\": 61617,    \"secure\": true,    \"type\": \"GENERAL_RELAY\"  }]"
```
