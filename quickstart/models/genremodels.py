from django.db import models

class Genre(models.Model):
    """
    Stores a single Genre,
    """
    name = models.CharField(max_length=55)

    def __str__(self):
        return 'Genre: {}'.format(self.name)