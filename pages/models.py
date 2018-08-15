from django.db import models

# Create your models here.
class Urls(models.Model):
    long = models.URLField()
    short = models.CharField(max_length=200)

    def __str__(self):
        return self.long

