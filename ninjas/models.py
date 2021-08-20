from django.db import models

# Create your models here.
class Ninjas(models.Model):
    name = models.CharField(max_length=45)
    color = models.CharField(max_length=45)

    def __repr__(self) -> str:
        return f'Ninja {self.name}'
