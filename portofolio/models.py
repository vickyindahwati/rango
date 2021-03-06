from django.db import models

# Create your models here.
class exercise(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(null=True,blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name
