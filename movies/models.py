from django.db import models

# Create your models here.

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name



class ContentList(models.Model):
    titile = models.CharField(max_length=250)
    storyline = models.CharField(max_length=500)
    genere = models.CharField(max_length=100)
    platform = models.ForeignKey(StreamingPlatform,on_delete=models.CASCADE, related_name= "content_list")
    release = models.DateField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titile



    