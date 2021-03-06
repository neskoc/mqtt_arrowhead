# System design

## System macro view

Arrowhead (AH) local cloud (*desktop linux*) with following 4 built in roles (services)
1. Authentication
2. Orchestrator (e.g. authorisation)
3. Service registry
4. Management Tool 
5. IoT Edge Gateway providing interface for
    - Service provider: python __AH-client 0__ (*Raspberry pi*)
        - Publish one service using MQTT protocol
        - Consumes ServiceDiscovery service using the HTTP protocol.
            - Have to register it’s published service to the ServiceRegistry via the ServiceDiscovery service.
    - AH-client 0 pushes data to MQTT-broker (*Mosquitto* on  *Desktop linux*):
        * python __AH-client 1__ as subscriber for the IoT that will be streamed to Mosquitto
        * python __mqtt-client 1__ publishing stream to mqtt-broker,
        * Seems like __ActiveMQ__ supports [MQTT-protocol](http://activemq.apache.org/mqtt.html) and will automatically map between JMS/NMS and MQTT clients. So it should be possible to configure Gateway to stream directly to mqtt-broker (Mosquitto). There is no need for __mqtt-client 1__.
    - Service consumer, (*FiPy esp32 dev board*)
        * Consumes at minimum three services
            - Orchestration
            - Authorisation
            - AH-Client 0 published service
        * python __AH-client 2__ for authorisation/authentication
        * python __mqtt-client 2__ as mqtt-consumer

### Preconfiguration

1. Set up AH local cloud
    - Configure orchestration and  security using the Management tool
    - Manually register all 3 AH-clients' certificates
    - Manually set up/configure authorization levels and services for each clients
    - Configure default streaming parameters (attributes)
2. Manually setup mqtt-broker (Mosquitto)
    - register ~~mqtt-client 1~~ __ActiveMQ__ as stream provider ~~inclusive generated certificate 1~~. To be investigate how certificate is going to be dealt with.
    - register __mqtt-client 2__ as mqtt-consumer inclusive generated certificate 2

### Activities

In parallell

- Service consumer (__AH-client 2__) through AH-gateway asks for authentication and authorisation
    - after authorisation it authenticates to mqtt-broker  
    and starts listening for data on the provided channel (topic)
- Service provider (__AH-client 0__) through AH-gateway starts authentication and authorisation
    1. after authorisation (it could change default streaming parameters as an option)  
    it starts providing data to subscribers: __AH-client 2__ (AH-gateway will provide it to subscribers)
    2. ~~Service consumer/subscriber (__AH-client 2__) is going to pull (GET) that data and~~
    3. ~~... as __mqtt-client 2__ = mqtt-provider push (publish) data for __AH-client 1__ through mqtt-broker~~
    4. AH Gateway through ActiveMQ starts publishing stream on mgtt-broker.
    5. Mosquitto is going to publish this data as topic for its consumers (__mqtt-client 2__)
    6. __mqtt-client 2__ as mqtt-consumer is going to pull published data from mqtt-broker

### TO DO

1. Install and configure all the necessary applications: AH-local cloud and Mosquitto
2. Generate and install necessary certificates
3. Set up accounts/authentication, roles and authorisation on AH-local cloud and Mosquitto
4. Write the following python scripts:
    - __AH-clients__: 0, ~~1~~ and 2
    - __mqtt-clients__: ~~1~~ and 2
5. Test
