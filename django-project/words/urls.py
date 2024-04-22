from django.urls import path

from . import views

urlpatterns = [
    # views.word_detail
    path('word/<str:word_text>/', views.word_detail, name='word_detail'),
]