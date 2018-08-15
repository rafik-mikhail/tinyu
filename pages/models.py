from django.db import models

# Create your models here.
class Urls(models.Model):
    long = models.URLField(unique=True)
    short = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.short

