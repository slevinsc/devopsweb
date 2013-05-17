from django.db import models

# Create your models here.


class username(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
