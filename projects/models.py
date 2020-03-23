from django.db import models

class Translation(models.Model):
    key = models.CharField(max_length=255)
    text_pl = models.TextField()
    text_en = models.TextField()

class Project(models.Model):
    title_obj = models.ForeignKey('Translation', related_name='translation_title', on_delete=models.CASCADE)
    short_description = models.ForeignKey('Translation', related_name='translation_short_description', on_delete=models.CASCADE)
    description = models.ForeignKey('Translation', related_name='translation_description', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    hyperlink = models.URLField()
    publication_date = models.DateTimeField(auto_now_add=True)