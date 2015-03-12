from django.db import models

# Create your models here.

class subs_info(models.Model):
    pass

class yonghu(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    agender=models.CharField(max_length=5)
    email=models.EmailField()
    def __unicode__(self):
        return self.name