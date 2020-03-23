from jobs.models import Configuration
from jobs.models import Translation as JOBS_TR
from blog.models import Translation as BLOG_TR
from projects.models import Translation as PROJ_TR

global_translations = dict()

class TranslationManager:
    _instance = None

    def __init__(self):
        self.current_language = 'en'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            instance = super().__new__(cls, *args, **kwargs)
            instance.current_language = 'en'
            cls._instance = instance
        return cls._instance

    def __get_current_language(self):
        return self.current_language

    def set_current_language(self, language: str):
        if language.lower() in ['english', 'en', 'us', 'england']:
            lang = 'en'
        else:
            lang = 'pl'
        self.current_language = lang

    def __get_translation_for_language(self, translation_obj):
        if self.current_language == 'en':
            return translation_obj.text_en
        else:
            return translation_obj.text_pl


    def get_translation(self, key):
        models = [JOBS_TR, BLOG_TR, PROJ_TR]
        for model in models:
            try:
                translation_obj = model.objects.get(key=key)
            except model.DoesNotExist:
                translation_obj = None
            if translation_obj:
                return self.__get_translation_for_language(translation_obj)
        return 'NOT_TRANSLATION_FOUND'

translator = TranslationManager()

def reload_global_translations_with_language(lang: str):
    translator.set_current_language(lang)
    global_translations['Resume'] = translator.get_translation('TR_RESUME')
    global_translations['Flag'] = translator.get_translation('TR_FLAG_FILE')
    global_translations['Blog'] = translator.get_translation('TR_BLOG')
    global_translations['TR_CV_FILENAME'] = translator.get_translation('TR_CV_FILENAME')
    global_translations['Donate'] = translator.get_translation('TR_DONATE_BUTTON')
    global_translations['Projects'] = translator.get_translation('TR_PROJECTS')
    global_translations['More'] = translator.get_translation('TR_MORE')
