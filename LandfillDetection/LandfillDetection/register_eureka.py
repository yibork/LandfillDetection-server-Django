# eureka_client_config.py
from py_eureka_client.eureka_client import EurekaClient

async def register_service():
    eureka_client = EurekaClient(
        eureka_server="http://localhost:8761/",
        app_name="django",
        instance_port=8001,
        instance_host="137.184.5.79",
    )
    await eureka_client.start()

async def deregister_service():
    await EurekaClient.stop()
