from django.contrib import admin
from .models import Job, Translation, Configuration, Skill

admin.site.register(Job)
admin.site.register(Translation)
admin.site.register(Configuration)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('summary', 'priority')
    ordering = ('priority', )