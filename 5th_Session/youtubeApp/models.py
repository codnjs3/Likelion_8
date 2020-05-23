from django.db import models

# Create your models here.
class Channel(models.Model):
    name = models.CharField(max_length=50)
    creator = models.CharField(max_length=50)
    fav = models.IntegerField()
    live = models.BooleanField()
    subscription = models.IntegerField()
    link1 = models.TextField()
    link2 = models.TextField()
    link3 = models.TextField()
    img1 = models.TextField()
    img2 = models.TextField()
    img3 = models.TextField()

    text = models.TextField(max_length=2000)
    summary = models.TextField(max_length=200)
    photo = models.ImageField(upload_to="image",blank=True)


    def __str__(self):
        return self.name