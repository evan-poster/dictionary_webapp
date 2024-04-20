# your_custom_command.py

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def handle(self, *args, **options):
        # Open the CSV file
        with open(options['filename'], 'r') as csvfile:
            # Read the CSV data
            reader = csv.reader(csvfile)
            for row in reader:
                # Process the row as needed
                pass
