from django.apps import AppConfig
from py_eureka_client import eureka_client


class LandfillManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Landfill_management'
    verbose_name = 'Landfill_management'
