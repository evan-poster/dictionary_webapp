from django.contrib import admin

from .models import Word, Definition

# Register models
admin.site.register(Word)
admin.site.register(Definition)
