from django.db import models

class Genre(models.Model):
    """
    Stores a single Genre in the db, the output given in the method below will allow the lable "Genre" to be displayed in the other models' views as a dropdown.  The only property in this class is "name"

    fields:
    'name' is a character field
    """
    name = models.CharField(max_length=55)

    def __str__(self):
        return 'Genre: {}'.format(self.name)