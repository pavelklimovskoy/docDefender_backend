from django.db import models


# Create your models here.

class FileModel(models.Model):
    file_name = models.CharField(max_length=256)
    time_upload = models.TimeField(auto_now=True)
    date_upload = models.DateField(auto_now=True)

    # file = models.FileField()
    file_path = models.CharField()
