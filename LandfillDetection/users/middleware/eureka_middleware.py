from django.core.signals import request_started
from django.dispatch import receiver
from py_eureka_client.eureka_client import EurekaClient

# Global variable to ensure registration happens only once
has_registered = False

@receiver(request_started)
def register_with_eureka(sender, **kwargs):
    global has_registered
    if not has_registered:
        eureka_client = EurekaClient(
            eureka_server="http://localhost:8761/eureka/",
            app_name="django",
            instance_port=8000,
            instance_host="10.126.86.225"
        )
        # Asynchronous registration needs to be handled appropriately
        # This might involve using Django's asynchronous views or running
        # the asynchronous code in a synchronous block using asgiref.sync.async_to_sync
        async_to_sync(eureka_client.register)()
        
        has_registered = True
from django.utils.deprecation import MiddlewareMixin
from asgiref.sync import async_to_sync

# Inside the register_with_eureka function

class EurekaRegistrationMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)

    def __call__(self, request):
        response = self.get_response(request)
        return response
