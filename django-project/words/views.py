from django.http import JsonResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

from .models import Word

def word_detail(request, word_text):
    """
    View for fetching a word
    """
    try:
        word = Word.objects.filter(word__iexact=word_text).get()
    except Word.DoesNotExist:
        return JsonResponse({'error': 'Word does not exist'}, status=404)

    # Serialize the word and its definitions
    data = {
        'word': word.word,
        'definitions': [{'definition': defn.definition, 'part_of_speech': defn.part_of_speech} for defn in word.definitions.all()],
    }

    # Combine the definitions with their parts of speech

    return JsonResponse(data)
