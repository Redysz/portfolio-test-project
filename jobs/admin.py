from django.contrib import admin
from .models import Job, Translation, Configuration, Skill

admin.site.register(Job)
admin.site.register(Translation)
admin.site.register(Configuration)
admin.site.register(Skill)
