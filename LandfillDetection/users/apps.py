from django.apps import AppConfig
import threading
from py_eureka_client.eureka_client import EurekaClient
import asyncio

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    eureka_client = None  # Class-level attribute to hold the Eureka client instance

    def start_eureka_client(self):
        async def async_start():
            UsersConfig.eureka_client = EurekaClient(
                eureka_server="http://localhost:8761/eureka/",
                app_name="django",
                instance_port=8001,
                instance_host="localhost",
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
        print("Starting Eureka Client")
        threading.Thread(target=self.start_eureka_client).start()
