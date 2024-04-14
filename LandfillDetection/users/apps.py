from django.apps import AppConfig
import threading
from py_eureka_client.eureka_client import EurekaClient
import asyncio
import socket
import os

def get_ip_address():
    """Utility to get the local IP address."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        IP = '127.0.0.1'
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    eureka_client = None
    def start_eureka_client(self):
        async def async_start():
            ip_address = get_ip_address()
            port_number = os.getenv('PORT', 8000)  
            UsersConfig.eureka_client = EurekaClient(
                eureka_server="http://yassine.fixi.website:8761/",
                app_name="django",
                instance_port=8001,
                instance_host='146.190.14.232',
            )
            await UsersConfig.eureka_client.start()
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(async_start())

    @staticmethod
    async def stop_eureka_client():
        if UsersConfig.eureka_client:
            await UsersConfig.eureka_client.stop()

    def ready(self):
        print("Starting Eureka Client with IP:", get_ip_address())
        threading.Thread(target=self.start_eureka_client).start()
