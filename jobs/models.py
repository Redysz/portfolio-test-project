from django.db import models

class Job(models.Model):
     image = models.ImageField(upload_to='images/')
     link = models.URLField()
     summary_pl = models.CharField(max_length=200)
     summary_en = models.CharField(max_length=200)

class Skill(models.Model):
     icon = models.ImageField(upload_to='images/')
     summary = models.CharField(max_length=50)


class Translation(models.Model):
     key = models.CharField(max_length=255)
     text_pl = models.TextField()
     text_en = models.TextField()

class Configuration(models.Model):
     key = models.CharField(max_length=255)
     value = models.TextField()