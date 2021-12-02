from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    release = models.DateField()

    def __str__(self):
        return self.name



    