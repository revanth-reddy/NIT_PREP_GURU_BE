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