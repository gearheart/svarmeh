import urllib
from itertools import count
from django.utils import simplejson as json
from django.template.defaultfilters import slugify as django_slugify

import logging
logger = logging.getLogger(__name__)


translate_url = 'https://ajax.googleapis.com/ajax/services/language/translate'

def get_translation(term, l1='ru', l2='en'):
    params = {
        'v': '1.0',
        'langpair': l1 + '|' + l2,
        'q': term.encode('utf-8'),
    }
    try:
        result = json.load(urllib.urlopen(translate_url + '?' + (urllib.urlencode(params))))
    except IOError, e:
        logger.warning('get_translation error: ' + str(e))
        return ''
    else:
        if result.get('responseStatus', None) == 200:
            return result['responseData']['translatedText']
        return ''

def slugify(term):
    return django_slugify(get_translation(term))

def unique_field(model, field, value):
    result = value

    for i in count(2):
        if not model.objects.filter(**{field: value}).exists():
            return result
        result = '%s-%s' % (value, i)

def get_slug(model, name):
    return unique_field(model, 'slug', slugify(name))

