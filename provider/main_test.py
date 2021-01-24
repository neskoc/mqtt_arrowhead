# time_provider.py
import arrowhead_client.api as ar

time_provider = ar.ArrowheadHttpClient('time_provider',
                               'localhost',
                               1337,
                               '',
                               keyfile='crypt/provider.key',
                               certfile='crypt/provider.pem')

what_to_hello = 'Arrowhead'

@time_provider.provided_service('echo', 'echo', 'HTTP-SECURITY_SECURE-JSON', 'GET', hello_what=what_to_hello)
def echo(request, hello_what) -> Dict[str, str]:
    return {'msg': f'Hello {hello_what}'}

############################################################
# api.py
from arrowhead_client.client import ArrowheadClient, provided_service

class ArrowheadHttpClient(ArrowheadClient):
    """
    Attributes: authentication_info: A string to assign the system authentication info
    """

    def __init__(self,
                 system_name: str,
                 address: str, # system address
                 port: int, # system port
                 config: Dict = None, # ? system authentication info
                 keyfile: str = '', # PEM keyfile
                 certfile: str = '', # PEM certfile
                 cafile: str = ''):
        logger = get_logger(system_name, 'debug')
        system = ArrowheadSystem.with_certfile(
                system_name,
                address,
                port,
                certfile,
        )
        super().__init__(
                system,
                HttpConsumer(keyfile, certfile, cafile),
                HttpProvider(cafile),
                logger,
                config=config,
                keyfile=keyfile,
                certfile=certfile
        )
        self._logger.info(f'{self.__class__.__name__} initialized at {self.system.address}:{self.system.port}')

############################################################
# client/__init__.py
from .client_core import ArrowheadClient, provided_service
__all__ = ['ArrowheadClient', 'provided_service']

############################################################
# client_core.py

def provided_service(
            service_definition: str,
            service_uri: str,
            protocol: str,
            method: str,
            payload_format: str,
            access_policy: str,
    ):
    """
    Decorator that can be used in custom client subclasses to define services.

    Returns:
        A ServiceDescriptor object
    """

class ArrowheadClient:
    """
    Application class for Arrowhead Systems. This class serves as a bridge that connects systems, consumers, and providers to the user.
    """

    def __init__(self,
                 system: ArrowheadSystem,
                 consumer: BaseConsumer,
                 provider: BaseProvider,
                 logger: Any, # will default to the logger found in logs.get_logger()
                 config: Dict = None,
                 keyfile: str = '', # PEM keyfile
                 certfile: str = '', ): # PEM certfile
        self.system = system
        self.consumer = consumer
        self.provider = provider
        self.keyfile = keyfile
        self.certfile = certfile
        self.secure = all(self.cert)
        self._logger = logger
        self.config = config or ar_config
        self.auth_authentication_info = None
        self.orchestration_rules = OrchestrationRuleContainer()
        self.registration_rules = RegistrationRuleContainer()
        # TODO: Should add_provided_service be exactly the same as the provider's,
        # or should this class do something on top of it?
        # It's currently not even being used so it could likely be removed.
        # Maybe it should be it's own method?
        self.add_provided_service = self.provider.add_provided_service

    __arrowhead_services__ = []
    
    # @provided_service('echo', 'echo', 'HTTP-SECURITY_SECURE-JSON', 'GET', hello_what='Arrowhead')
    def provided_service(
            self,
            service_definition: str, # to be stored in the provided_service registry
            service_uri: str, # The path to the provided_service
            protocol: str,
            method: str, # HTTP method required to access the provided_service
            payload_format: str,
            access_policy: str,
    ) -> Callable:

        provided_service = Service(
                service_definition,
                service_uri,
                ServiceInterface.with_access_policy(
                        protocol,
                        access_policy,
                        payload_format,
                ),
                access_policy,
        )

        def wrapped_func(func):
            self.registration_rules.store(
                    RegistrationRule(
                            provided_service,
                            self.system,
                            method,
                            func,
                    )
            )
            return func

        return wrapped_func

############################################################
