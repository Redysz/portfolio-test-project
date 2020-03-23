from django.shortcuts import render, redirect
from blog.models import Blog
from blog.traslation_manager import translator, global_translations, reload_global_translations_with_language
from blog.utils import get_lang_from_request

def allblogs(request):
    blogs = Blog.objects.all()
    reload_global_translations_with_language(get_lang_from_request(request))
    return render(request, 'blog/allblogs.html', {'blogs': blogs, 'translations': global_translations})

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    reload_global_translations_with_language(get_lang_from_request(request))
    return render(request, 'blog/detail.html', {'blog': blog, 'translations': global_translations})

def change_lang(request, lang):
    translator.set_current_language(language=lang)
    request.session['lang'] = lang
    reload_global_translations_with_language(lang)
    return redirect(request.META['HTTP_REFERER'])