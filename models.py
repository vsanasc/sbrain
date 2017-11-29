from django.db import models

LANGUAGES = {
    'af' : 'Afrikaans',
    'sq' : 'Albanian',
    'ar' : 'Arabic',
    'hy' : 'Armenian',
    'bn' : 'Bengali',
    'ca' : 'Catalan',
    'zh' : 'Chinese',
    'zh-cn' : 'Chinese (Mandarin/China)',
    'zh-tw' : 'Chinese (Mandarin/Taiwan)',
    'zh-yue' : 'Chinese (Cantonese)',
    'hr' : 'Croatian',
    'cs' : 'Czech',
    'da' : 'Danish',
    'nl' : 'Dutch',
    'en' : 'English',
    'en-au' : 'English (Australia)',
    'en-uk' : 'English (United Kingdom)',
    'en-us' : 'English (United States)',
    'eo' : 'Esperanto',
    'fi' : 'Finnish',
    'fr' : 'French',
    'de' : 'German',
    'el' : 'Greek',
    'hi' : 'Hindi',
    'hu' : 'Hungarian',
    'is' : 'Icelandic',
    'id' : 'Indonesian',
    'it' : 'Italian',
    'ja' : 'Japanese',
    'km' : 'Khmer (Cambodian)',
    'ko' : 'Korean',
    'la' : 'Latin',
    'lv' : 'Latvian',
    'mk' : 'Macedonian',
    'no' : 'Norwegian',
    'pl' : 'Polish',
    'pt' : 'Portuguese',
    'ro' : 'Romanian',
    'ru' : 'Russian',
    'sr' : 'Serbian',
    'si' : 'Sinhala',
    'sk' : 'Slovak',
    'es' : 'Spanish',
    'es-es' : 'Spanish (Spain)',
    'es-us' : 'Spanish (United States)',
    'sw' : 'Swahili',
    'sv' : 'Swedish',
    'ta' : 'Tamil',
    'th' : 'Thai',
    'tr' : 'Turkish',
    'uk' : 'Ukrainian',
    'vi' : 'Vietnamese',
    'cy' : 'Welsh'
}

class Producer(models.Model):
	name = models.CharField(max_length=50)


class Production(models.Model):
	producer = models.ForeignKey('Producer')
	name = models.CharField(max_length=50)


class Phrase(models.Model):
	text = models.CharField(max_length=100)
	lang = models.CharField(max_length=2)
	variation = models.CharField(max_length=3)


class PhraseAudio(models.Model):
	phrase = models.ForeignKey('Phrase')


class Relation(models.Model):
	pass



