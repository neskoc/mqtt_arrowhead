"""
HttpConsumer example app
"""
import arrowhead_client.api as ar

consumer = ar.ArrowheadHttpClient(
        system_name='consumer',
        address='127.0.0.1',
        port=7656,
        keyfile='crypt/consumer-app.key',
        certfile='crypt/consumer-app.pem'
)


if __name__ == '__main__':
    consumer.setup()

    consumer.add_orchestration_rule('hello-arrowhead', 'GET')
    response = consumer.consume_service('hello-arrowhead')
    print(response.read_json()['msg'])

    consumer.add_orchestration_rule('echo', 'PUT')
    echo_response = consumer.consume_service('echo', json={'msg': 'ECHO'})
    print(echo_response.read_json()['msg'])
