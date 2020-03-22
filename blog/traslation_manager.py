from jobs.models import Configuration
from jobs.models import Translation as JOBS_TR
from blog.models import Translation as BLOG_TR

global_translations = dict()

class TranslationManager:
    _instance = None

    def __init__(self):
        self.current_language = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instance = instance
        return cls._instance

    def __get_current_language(self):
        self.current_language = Configuration.objects.get(key='language').value

    @staticmethod
    def set_current_language(language: str):
        if language.lower() in ['english', 'en', 'us', 'england']:
            lang = 'en'
        else:
            lang = 'pl'
        conf = Configuration.objects.get(key='language')
        conf.value = lang
        conf.save()

    def __get_translation_for_language(self, translation_obj):
        self.__get_current_language()
        if self.current_language == 'en':
            return translation_obj.text_en
        else:
            return translation_obj.text_pl


    def get_translation(self, key):
        models = [JOBS_TR, BLOG_TR]
        for model in models:
            try:
                translation_obj = model.objects.get(key=key)
            except JOBS_TR.DoesNotExist:
                translation_obj = None
            if translation_obj:
                return self.__get_translation_for_language(translation_obj)
        return 'NOT_TRANSLATION_FOUND'

translator = TranslationManager()

def reload_global_translations():
    global_translations['Resume'] = translator.get_translation('TR_RESUME')
    global_translations['Flag'] = translator.get_translation('TR_FLAG_FILE')
    global_translations['Blog'] = translator.get_translation('TR_BLOG')
    global_translations['TR_CV_FILENAME'] = translator.get_translation('TR_CV_FILENAME')

reload_global_translations()