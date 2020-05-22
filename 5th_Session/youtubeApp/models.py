from django.db import models

# Create your models here.
class Channel(models.Model):
    name = models.CharField(max_length=50)
    creater = models.CharField(max_length=50)
    fav = models.IntegerField()
    live = models.BooleanField()
    subscription = models.IntegerField()
    link1 = models.TextField()
    link2 = models.TextField()
    link3 = models.TextField()
    img1 = models.TextField()
    img2 = models.TextField()
    img3 = models.TextField()


    def __str__(self):
        return self.name