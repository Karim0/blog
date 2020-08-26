from django.db import models
from django.utils.html import mark_safe


# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=256)
    desc = models.TextField()

    def __str__(self):
        return self.name


class FlowerPhoto(models.Model):
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='flowers/')

    def __str__(self):
        return self.img.name

    def image_tag(self):
        return mark_safe(f'<img style="width:200px; height=200px" src="{self.img.url}" />')
