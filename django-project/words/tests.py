from django.test import TestCase
from django.db.utils import IntegrityError

from .models import Word, Definition

class WordModelTests(TestCase):
    def test_word_model_can_create_word(self):
        """Word model can create a Word."""
        Word.objects.create(word='test_word')
        word = Word.objects.get(word='test_word')
        self.assertEqual(word.word, 'test_word')


class DefinitionModelTests(TestCase):
    def setUp(self):
        self.test_word = Word.objects.create(word='test_word')

    def test_definition_model_can_create_definition(self):
        """Definition model can create a Definition."""
        Definition.objects.create(word=self.test_word,
                                  part_of_speech='noun',
                                  definition='test_definition')
        definition = Definition.objects.get(word=self.test_word)
        self.assertEqual(definition.definition, 'test_definition')

