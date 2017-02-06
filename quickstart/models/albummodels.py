from django.db import models
from .genremodels import Genre
from .artistmodels import Artist

class Album(models.Model):
    """
    Stores a single Album
    fields:
    'name' is a character field
    'genre' is a foreign key
    'artist' is a foreign key
    """
    name = models.CharField(max_length=55)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return 'Album: {}'.format(self.name)