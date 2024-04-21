# your_custom_command.py
# data is stored in a CSV file with three columns: word, part_of_speech, definition
from django.conf import settings
from django.core.management.base import BaseCommand
import csv, os

from words.models import Word, Definition


# File is in the data/ folder in the root of the project
filename = os.path.join(settings.BASE_DIR) + '/data/dictionary.csv'


class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def handle(self, *args, **options):
        # Open the CSV file
        with open(filename, 'r') as csvfile:
            # Read the CSV data
            reader = csv.reader(csvfile)
            for row in reader:
                # Get or Create the Word
                word, word_created = Word.objects.get_or_create(word=row[0])
                # Get or Create the Definition
                definition, def_created = Definition.objects.get_or_create(word=word, part_of_speech=row[1], definition=row[2])
                # Save both objects if they were created
                if word_created:
                    word.save()
                if def_created:
                    definition.save()
