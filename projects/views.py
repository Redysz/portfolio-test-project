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
    project_obj = Project.objects.get(id=project_id)
    lang = get_lang_from_request(request)
    reload_global_translations_with_language(lang)
    if lang == 'en':
        project = {'id': project_obj.pk,
                   'title': project_obj.title_obj.text_en,
                   'second_title': getattr(project_obj.second_title, 'text_en', None),
                   'short_description': project_obj.short_description.text_en,
                   'description': project_obj.description.text_en,
                   'image': project_obj.image,
                   'hyperlink': getattr(project_obj.hyperlink, 'text_en', None),
                   'hyperlink_title': getattr(project_obj.hyperlink_title, 'text_en', None)
                   }
    else:
        project = {'id': project_obj.pk,
                   'title': project_obj.title_obj.text_pl,
                   'second_title': getattr(project_obj.second_title, 'text_pl', None),
                   'short_description': project_obj.short_description.text_pl,
                   'description': project_obj.description.text_pl,
                   'image': project_obj.image,
                   'hyperlink': getattr(project_obj.hyperlink, 'text_pl', None),
                   'hyperlink_title': getattr(project_obj.hyperlink_title, 'text_pl', None)
                   }

        images = [project_obj.gallery_image1, project_obj.gallery_image2,
                  project_obj.gallery_image3, project_obj.gallery_image4]
        not_none_images = []
        for image in images:
            if bool(image.name):
                not_none_images.append(image)
        project['gallery'] = not_none_images

    return render(request, 'projects/detail.html', {'project': project, 'translations': global_translations})