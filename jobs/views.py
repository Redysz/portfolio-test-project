from django.shortcuts import render
from .models import Job
from blog.traslation_manager import translator, global_translations, reload_global_translations_with_language
from blog.utils import get_lang_from_request

def home(request):
    jobs = Job.objects.all().order_by('-id')[:4]
    translations = dict()
    reload_global_translations_with_language(get_lang_from_request(request))
    translations['Hello'] = translator.get_translation('TR_HELLO')
    translations['Welcome'] = translator.get_translation('TR_WELCOME')
    translations['Write'] = translator.get_translation('TR_WRITE_TO_ME')
    translations.update(global_translations)
    return render(request, 'jobs/home.html', {'jobs':jobs, 'translations': translations})

def donate(request):
    translations = dict()
    reload_global_translations_with_language(get_lang_from_request(request))
    translations['Support'] = translator.get_translation('TR_SUPPORT')
    translations['SupportText'] = translator.get_translation('TR_SUPPORT_TEXT')
    translations['BuyCourses'] = translator.get_translation('TR_BUY_COURSES')
    translations['GotoProjects'] = translator.get_translation('TR_GO_TO_PROJECTS')
    translations['TransferMoney'] = translator.get_translation('TR_TRANSFERRING_MONEY')
    translations['TraditionalTransfer'] = translator.get_translation('TR_TRADITIONAL_TRANSFER')
    translations['BankAccount'] = translator.get_translation('TR_BANK_ACCOUNT')
    translations['AccountNumber'] = translator.get_translation('TR_ACCOUNT_NUMBER')
    translations['Recipient'] = translator.get_translation('TR_RECIPIENT')
    translations['TransferTitle'] = translator.get_translation('TR_TRANSFER_TITLE')
    translations['Donation'] = translator.get_translation('TR_DONATION')
    translations['AdditionalInfo'] = translator.get_translation('TR_ADDITIONAL_INFO')
    translations['ChooseCurrency'] = translator.get_translation('TR_CHOOSE_CURRENCY')
    translations['Name'] = translator.get_translation('TR_NAME')
    translations['Address1'] = translator.get_translation('TR_ADDRESS_1')
    translations['Address2'] = translator.get_translation('TR_ADDRESS_2')
    translations['Country'] = translator.get_translation('TR_COUNTRY')
    translations.update(global_translations)
    return render(request, 'jobs/donate.html', {'translations': translations})