from django.shortcuts import render
from projects.models import Translation, Project
from blog.traslation_manager import translator, global_translations, reload_global_translations_with_language
from blog.utils import get_lang_from_request

def allprojects(request):
    projects = Project.objects.all()
    lang = get_lang_from_request(request)
    reload_global_translations_with_language(lang)
    my_projects = list()
    for project in projects:
        if lang == 'en':
            my_projects.append({'id': project.pk,
                                'title': project.title_obj.text_en,
                                'short_description': project.short_description.text_en,
                                'description': project.description.text_en,
                                'image': project.image,
                                'hyperlink': project.hyperlink
                                })
        else:
            my_projects.append({'id': project.pk,
                                'title': project.title_obj.text_pl,
                                'short_description': project.short_description.text_pl,
                                'description': project.description.text_pl,
                                'image': project.image,
                                'hyperlink': project.hyperlink
                                })
    return render(request, 'projects/allprojects.html', {'projects': my_projects, 'translations': global_translations})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    reload_global_translations_with_language(get_lang_from_request(request))
    return render(request, 'projects/detail.html', {'project': project, 'translations': global_translations})