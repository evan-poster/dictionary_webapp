from django.shortcuts import render

# JSON Response for a word

from django.http import JsonResponse
from .models import Word


def word_detail(request, word_text):
    """
    View for fetching a word
    """
    try:
        word = Word.objects.get(word=word_text)
    except Word.DoesNotExist:
        return JsonResponse({'error': 'Word does not exist'}, status=404)

    data = {
        'word': word.word,
        'definitions': [defn.definition for defn in word.definitions.all()],
        'part_of_speeches': [defn.part_of_speech for defn in word.definitions.all()],
    }

    return JsonResponse(data)
