from django.db import models

class Blog(models.Model):
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    publication_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)

# Add the Blog app to the settings

# create a migration

# Migrate

# Add to the admin