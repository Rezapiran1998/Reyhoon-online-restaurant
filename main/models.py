from django.db import models

# Create your models here.

class Resturant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    # tags = models.ManyToManyField('Tag')
    rate = models.IntegerField(default=0)
    natural_tag = models.BooleanField(default=True)
    warranty_tag = models.BooleanField(default=False)


    def __str__(self):
        return self.name


