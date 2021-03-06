from django.db import models
from .genremodels import Genre

class Artist(models.Model):
    """
    Stores a single Artist
    fields:
    'name' is a character field
    'genre' is a foreign key
    """
    name = models.CharField(max_length=55)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return 'Artist: {}'.format(self.name)
