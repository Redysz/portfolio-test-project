from django.db import models

class Job(models.Model):
     image = models.ImageField(upload_to='images/')
     summary = models.CharField(max_length=200)


class Translation(models.Model):
     key = models.CharField(max_length=255)
     text_pl = models.TextField()
     text_en = models.TextField()

class Configuration(models.Model):
     key = models.CharField(max_length=255)
     value = models.TextField()