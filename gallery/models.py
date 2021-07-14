from django.db import models
from directory.models import Person, Artist


class Art_Pieces(models.Model):
    PEOPLE = 'PPLE'
    OBJECTS = 'OBJCT'
    ABSTRACT = 'ABST'
    BUILDINGS = 'BUIL'
    LOCATIONS = 'LOCA'
    ANIMAL = 'ANIM'

    ARTWORK_CATEOGERY = [
        (PEOPLE, 'People'),
        (OBJECTS, 'Objects'),
        (ABSTRACT, 'Abstract'),
        (BUILDINGS, 'Buildings'),
        (LOCATIONS, 'Location'),
        (ANIMAL, 'Animal'),
    ]

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    # TODO: why CASCADE artist foreign key on delete instead of SET_NULL???
    # category = models.ForeignKey('Artwork_Cat', on_delete=models.CASCADE, 
    # null=False, blank=False)

    category = models.CharField(
        max_length=20,
        choices=ARTWORK_CATEOGERY)

    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=120, null=False, blank=True)
    size_heigth = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    size_width = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.title


class Comment(models.Model):

    art_piece = models.ForeignKey(Art_Pieces, on_delete=models.CASCADE)
    date = models.DateTimeField('Comment Date')
    text = models.TextField('Comment')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Rate(models.Model):

    class Rating(models.IntegerChoices):
        POOR = 1
        OK = 2
        GOOD = 3
        VERY_GOOD = 4
        EXCELLENT = 5

    art_piece = models.ForeignKey(Art_Pieces, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Rating.choices)

    def __str__(self):
        return self.art_piece
