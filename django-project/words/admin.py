from django.contrib import admin

from .models import Word, Definition, Source

# Register models
admin.site.register(Word)
admin.site.register(Definition)
admin.site.register(Source)
