from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    port = models.IntegerField()
    last_heartbeat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
