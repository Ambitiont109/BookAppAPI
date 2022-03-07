from django.db import models


# Create your models here.
class GenreList(models.TextChoices):
    Action = 'Action'
    Classics = 'Classics'
    Comic = 'Comic'
    Detective = 'Detective'
    Fantasy = 'Fantasy'
    Horror = 'Horror'
    LiteraryFiction = 'LF', 'Literary Fiction'

class Book(models.Model):
    author = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    synopsis = models.TextField()
    genere = models.CharField(max_length=50, choices=GenreList.choices, default=GenreList.Action)
    released_date = models.DateField()
    price = models.IntegerField(default=0) # 100 cents = 1$
