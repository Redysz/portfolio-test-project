from django.shortcuts import render
from .models import Job
from blog.traslation_manager import translator, global_translations

def home(request):
    jobs = Job.objects
    translations = dict()
    translations['Hello'] = translator.get_translation('TR_HELLO')
    translations['Welcome'] = translator.get_translation('TR_WELCOME')
    translations['Write'] = translator.get_translation('TR_WRITE_TO_ME')
    translations.update(global_translations)
    return render(request, 'jobs/home.html', {'jobs':jobs, 'translations': translations})