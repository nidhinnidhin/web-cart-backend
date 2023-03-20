from django.db import models

# Create your models here.

class Slider(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(null=True, upload_to = '')
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.name 