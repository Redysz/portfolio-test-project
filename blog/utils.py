def get_lang_from_request(request):
    lang = 'en'
    if 'lang' in request.session:
        lang = request.session['lang']
        if lang.lower() in ['english', 'en', 'us', 'england']:
            lang = 'en'
        else:
            lang = 'pl'
    request.session['lang'] = lang
    return lang