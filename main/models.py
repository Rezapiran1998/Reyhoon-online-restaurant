from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Resturant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    # tags = models.ManyToManyField('Tag')
    rate = models.IntegerField(default=0)
    natural_tag = models.BooleanField(default=True)
    warranty_tag = models.BooleanField(default=False)

    def __str__(self):
        return self.name


