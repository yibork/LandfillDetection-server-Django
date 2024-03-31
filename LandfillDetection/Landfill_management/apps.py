from django.apps import AppConfig
from py_eureka_client import eureka_client


class LandfillManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Landfill_management'
    verbose_name = 'Landfill_management'
    eureka_server_url = "http://localhost:8761/eureka/"
    app_name = "django"
    instance_port = 8001  # The port your Django app is running on
    instance_host = "10.126.113.181"  # Replace with the non-loopback IP address of your machine

        # Initialize and register with Eureka server
    eureka_client.init(
            eureka_server=eureka_server_url,
            app_name=app_name,
            instance_port=instance_port,
            instance_host=instance_host,  # Specify the non-loopback host of your instance
            home_page_url=f"http://{instance_host}:{instance_port}/",
            status_page_url=f"http://{instance_host}:{instance_port}/api/v1/Diet/",
            health_check_url=f"http://{instance_host}:{instance_port}/",
        )