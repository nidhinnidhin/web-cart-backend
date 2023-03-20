from django.db import models

# Create your models here.

class Announcement(models.Model):
    announcement = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.announcement