from django.db import models
from .albummodels import Album
from .artistmodels import Artist
from .genremodels import Genre

class Song(models.Model):
    """
    Stores a single Song,
    """
    name = models.CharField(max_length=55)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return "The song {}, recorded by {} on the album {}, falls into the {} genre.".format(self.name, self.artist, self.album, self.genre)

