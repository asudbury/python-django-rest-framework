from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    # what to print when it needs to print out an instance of the Hero model.
    def __str__(self):
        return self.name
