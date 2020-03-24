from django.db import models

class Translation(models.Model):
    key = models.CharField(max_length=255)
    text_pl = models.TextField()
    text_en = models.TextField()

class Project(models.Model):
    title_obj = models.ForeignKey('Translation', related_name='translation_title', on_delete=models.CASCADE)
    second_title = models.ForeignKey('Translation', related_name='translation_second_title', on_delete=models.CASCADE, null=True, blank=True)
    short_description = models.ForeignKey('Translation', related_name='translation_short_description', on_delete=models.CASCADE)
    description = models.ForeignKey('Translation', related_name='translation_description', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    gallery_image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    gallery_image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    gallery_image3 = models.ImageField(upload_to='images/', null=True, blank=True)
    gallery_image4 = models.ImageField(upload_to='images/', null=True, blank=True)
    hyperlink = models.URLField()
    hyperlink_title = models.ForeignKey('Translation', related_name='translation_hyperling_title', on_delete=models.CASCADE, null=True)
    publication_date = models.DateTimeField(auto_now_add=True)