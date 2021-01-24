"""
HttpProvider example app
"""
import arrowhead_client.api as ar

provider = ar.ArrowheadHttpClient(
        system_name='provider',
        address='127.0.0.1',
        port=7655,
        keyfile='crypt/provider.key',
        certfile='crypt/provider.pem'
        )


@provider.provided_service(
        'hello-arrowhead',
        'hello',
        'HTTP-SECURE-JSON',
        'GET',
        payload_format='JSON',
        access_policy='TOKEN')
def hello_arrowhead(request):
    return {"msg": "Hello, Arrowhead!"}

if __name__ == '__main__':
    provider.setup()
    provider.run_forever()
