from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    title = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=30, blank=True, default='')

    def __str__(self) :
        return self.name
