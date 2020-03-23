from django.shortcuts import render
from projects.models import Translation, Project
from blog.traslation_manager import translator, global_translations, reload_global_translations_with_language
from blog.utils import get_lang_from_request

def allprojects(request):
    projects = Project.objects.all()
    reload_global_translations_with_language(get_lang_from_request(request))
    return render(request, 'projects/allprojects.html', {'projects': projects, 'translations': global_translations})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    reload_global_translations_with_language(get_lang_from_request(request))
    return render(request, 'projects/detail.html', {'project': project, 'translations': global_translations})