from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

from words.views import svelte_app

urlpatterns = [
    path('admin/', admin.site.urls),
    # API routes
    path('api/', include('words.urls')),
]
