from django.shortcuts import render
from .models import Job, Skill
from blog.traslation_manager import translator, global_translations, reload_global_translations_with_language
from blog.utils import get_lang_from_request
from django.core.mail import send_mail
from .util import decrypt, encrypt, decrypt_rot13, encrypt_rot13
from not_commit.utils import forbidden_messages, forbidden_titles, check_for_spam


def home(request):
    jobs = Job.objects.all().order_by('-priority', '-id')[:4]
    skills = Skill.objects.all().order_by('-priority')
    translations = dict()
    lang = get_lang_from_request(request)
    reload_global_translations_with_language(lang)
    translations['Hello'] = translator.get_translation('TR_HELLO')
    translations['Welcome'] = translator.get_translation('TR_WELCOME')
    translations['Write'] = translator.get_translation('TR_WRITE_TO_ME')
    translations['lang'] = lang
    translations.update(global_translations)
    return render(request, 'jobs/home.html', {'jobs': jobs, 'skills': skills, 'translations': translations})


def donate(request):
    translations = dict()
    lang = get_lang_from_request(request)
    reload_global_translations_with_language(lang)
    translations['Support'] = translator.get_translation('TR_SUPPORT')
    translations['SupportText'] = translator.get_translation('TR_SUPPORT_TEXT')
    translations['BuyCourses'] = translator.get_translation('TR_BUY_COURSES')
    translations['GotoProjects'] = translator.get_translation('TR_GO_TO_PROJECTS')
    translations['ContactMePoint'] = translator.get_translation('TR_CONTACT_ME_POINT')
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


def contact(request):
    lang = get_lang_from_request(request)
    reload_global_translations_with_language(lang)
    return render(request, 'jobs/contact.html', {'translations': global_translations})


def our_own_encryption(request):
    if request.method == 'POST':
        if not request.POST['message']:
            return render(request, 'jobs/encryption.html', {})
        message = request.POST['message']
        if not request.POST['direction']:
            return render(request, 'jobs/encryption.html', {'message': message})
        direction = request.POST['direction']

        encryption = request.POST.get('encryption')
        if not encryption:
            encryption = 'unicode'

        if direction == 'decrypt':
            if encryption == 'unicode':
                message_then = decrypt(message)
            else:
                message_then = decrypt_rot13(message)
        else:
            if encryption == 'unicode':
                message_then = encrypt(message)
            else:
                message_then = encrypt_rot13(message)
        return render(request, 'jobs/encryption.html', {'message': message, 'message_then': message_then})

    return render(request, 'jobs/encryption.html', {})


def send_email_view(request):
    lang = get_lang_from_request(request)
    reload_global_translations_with_language(lang)
    if request.method == 'POST':
        if not request.POST['subject'] or not request.POST['message'] or not request.POST['sender_email'] or not request.POST['sender']:
            return render(request, 'jobs/contact.html',
                          {'translations': global_translations, 'error': global_translations['ContactError']})
        subject = str(request.POST['subject'])
        message = str(request.POST['message'])
        sender_email = str(request.POST['sender_email'])
        sender = str(request.POST['sender'])
        success = global_translations['EmailSuccess']
        if len(subject + message + sender_email + sender) > 5000:
            return render(request, 'jobs/contact.html',
                          {'translations': global_translations, 'success': success})
        for forbidden_title in forbidden_titles:
            if subject.lower() == forbidden_title:
                return render(request, 'jobs/contact.html',
                              {'translations': global_translations, 'success': success})
        for forbidden_message in forbidden_messages:
            if forbidden_message in message.lower():
                return render(request, 'jobs/contact.html',
                              {'translations': global_translations, 'success': success})
        check_for_spam(subject, sender_email, sender, message)
        send_mail(subject, sender_email+'\n'+sender+'\n'+message, 'karol.kurek.sender@gmail.com', ['karol.kurek.projects@gmail.com'],
                  fail_silently=False,
                  )
        return render(request, 'jobs/contact.html',
                      {'translations': global_translations, 'success': success})
    return render(request, 'jobs/contact.html', {'translations': global_translations})