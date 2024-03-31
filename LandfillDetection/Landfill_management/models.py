from django.db import models

class Record(models.Model):
    id = models.UUIDField(primary_key=True)  # Assuming you want to keep UUID as ID
    lat = models.FloatField()
    lng = models.FloatField()
    status = models.CharField(max_length=50)
    locality = models.CharField(max_length=100)

    def __str__(self):
        return self.locality
