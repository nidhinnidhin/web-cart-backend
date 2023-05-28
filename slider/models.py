from django.db import models

# Create your models here.

class Slider(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, upload_to = '')

    def __str__(self):
        return self.name 