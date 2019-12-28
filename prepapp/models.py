from django.db import models
import os

# Create your models here.
def slide_image_path(instance_id,filename):
        return os.path.join('slideshow',str(instance_id),filename)

class Slideshow(models.Model):
    image = models.ImageField(upload_to=slide_image_path)
    slide_link = models.CharField(max_length=120)
    order = models.IntegerField()
    class Meta:
        verbose_name_plural = "Slideshow"
    def str(self):
        return self.slide_link

class News(models.Model):
    news = models.TextField(max_length=500)
    link = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "News"
    def str(self):
        return self.news

class Companies(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Companies"
    def str(self):
        return self.name
