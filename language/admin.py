from django.contrib import admin

from language.models import (
    Generator,
    Phrase,
    PhraseAudio,
    RelationPhrase,
    Producer,
    Production,
    Season,
    Episode
)

admin.site.register(Generator)
admin.site.register(Phrase)
admin.site.register(PhraseAudio)
admin.site.register(RelationPhrase)
admin.site.register(Producer)
admin.site.register(Production)
admin.site.register(Season)
admin.site.register(Episode)
