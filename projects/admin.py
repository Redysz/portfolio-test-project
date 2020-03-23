from django.contrib import admin
from .models import Translation, Project

admin.site.register(Project)
admin.site.register(Translation)