from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Generator)
admin.site.register(Phrase)
admin.site.register(PhraseAudio)
admin.site.register(RelationPhrase)
admin.site.register(Producer)
admin.site.register(Production)
admin.site.register(Season)
admin.site.register(Episode)
