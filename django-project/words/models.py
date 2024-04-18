from django.db import models

# Source model
class Source():
    # Fields
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    # Methods
    def __str__(self):
        return self.name


# Words model
class Word(models.Model):
    # Fields
    word = models.CharField(max_length=255)

    # Methods
    def __str__(self):
        return self.word


class Definition(models.Model):
    # Fields
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    definition = models.TextField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    # Methods
    def __str__(self):
        return self.definition
