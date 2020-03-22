from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

class Translation(models.Model):
    key = models.CharField(max_length=255)
    text_pl = models.TextField()
    text_en = models.TextField()
