from django.conf import settings

NAME = getattr(settings, 'PUBLICATION_NAME', 'The Example Times')
LANG = getattr(settings, 'PUBLICATION_LANGUAGE', getattr(settings, 'LANGUAGE_CODE', 'en')).split('-')[0]