from jobs.models import Configuration
from jobs.models import Translation as JobsTr
from blog.models import Translation as BlogTr
from projects.models import Translation as ProjTr

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
        models = [JobsTr, BlogTr, ProjTr]
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
    global_translations['ContactTab'] = translator.get_translation('TR_CONTACT_TAB')
    global_translations['TR_CV_FILENAME'] = translator.get_translation('TR_CV_FILENAME')
    global_translations['Donate'] = translator.get_translation('TR_DONATE_BUTTON')
    global_translations['Projects'] = translator.get_translation('TR_PROJECTS')
    global_translations['More'] = translator.get_translation('TR_MORE')
    global_translations['BackToProjects'] = translator.get_translation('TR_BACK_TO_PROJECTS')
    global_translations['ProjectDescription'] = translator.get_translation('TR_PROJECT_DESCRIPTION')
    global_translations['ProjectDetails'] = translator.get_translation('TR_PROJECT_DETAILS')
    global_translations['Gallery'] = translator.get_translation('TR_GALLERY')
    global_translations['Newest'] = translator.get_translation('TR_NEWEST')
    global_translations['ContactTitle'] = translator.get_translation('TR_CONTACT_TITLE')
    global_translations['ContactError'] = translator.get_translation('TR_CONTACT_ERROR')
    global_translations['EmailSuccess'] = translator.get_translation('TR_EMAIL_SUCCESS')
    global_translations['ContactMe'] = translator.get_translation('TR_CONTACT_ME')
    global_translations['YourName'] = translator.get_translation('TR_YOUR_NAME')
    global_translations['YourEmail'] = translator.get_translation('TR_YOUR_EMAIL')
    global_translations['Subject'] = translator.get_translation('TR_SUBJECT')
    global_translations['YourMessage'] = translator.get_translation('TR_YOUR_MESSAGE')
    global_translations['Send'] = translator.get_translation('TR_SEND')
