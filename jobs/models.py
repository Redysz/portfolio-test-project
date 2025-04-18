from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    link = models.URLField()
    summary_pl = models.CharField(max_length=200)
    summary_en = models.CharField(max_length=200)
    priority = models.IntegerField(default=0)


class Skill(models.Model):
    icon = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=50)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.summary


class Translation(models.Model):
    key = models.CharField(max_length=255)
    text_pl = models.TextField()
    text_en = models.TextField()


class Configuration(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField()