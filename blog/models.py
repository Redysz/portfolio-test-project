from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
