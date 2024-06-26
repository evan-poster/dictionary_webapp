from django.db import models


# Words model
class Word(models.Model):
    # Fields
    word = models.CharField(max_length=255, unique=True)

    # Methods
    def __str__(self):
        return self.word

    class Meta:
        ordering = ['word']


class Definition(models.Model):
    # Fields: Word, Part of Speech, and Definition
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name="definitions")
    part_of_speech = models.CharField(max_length=255)
    definition = models.TextField()

    # Methods
    def __str__(self):
        return f"{self.word} - {self.definition[:20]}"  # self.definition

    class Meta:
        ordering = ['word', 'part_of_speech', 'definition']
