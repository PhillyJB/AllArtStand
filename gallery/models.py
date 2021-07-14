from django.db import models
from directory.models import Artist


class Art_Pieces(models.Model):
    OIL_PAINT = 'OIL'
    WATER_PAINT = 'WATER'
    ABSTRACT = 'ABSTRACT'
    BUILDINGS = 'BUILDING'
    ANIMAL = 'ANIMAL'

    ARTWORK_CATEOGERY = [
        (OIL_PAINT, 'Oil paintings'),
        (WATER_PAINT, 'Water paintings'),
        (ABSTRACT, 'Abstract'),
        (BUILDINGS, 'Buildings'),
        (ANIMAL, 'Animal'),
    ]
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=120)
    # TODO: Add standard sizes or test for correct format (BXH) (maybe?)
    size = models.CharField(max_length=10) 
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Artwork_Cat(models.Model):
    OIL_PAINT = 'OIL'
    WATER_PAINT = 'WATER'
    ABSTRACT = 'ABSTRACT'
    BUILDINGS = 'BUILDING'
    ANIMAL = 'ANIMAL'

    ARTWORK_CATEOGERY = [
        (OIL_PAINT, 'Oil paintings'),
        (WATER_PAINT, 'Water paintings'),
        (ABSTRACT, 'Abstract'),
        (BUILDINGS, 'Buildings'),
        (ANIMAL, 'Animal'),
    ]
    art_piece = models.ForeignKey(Art_Pieces, on_delete=models.CASCADE)
    specalistion = models.CharField(
        max_length=20,
        choices=ARTWORK_CATEOGERY,
    )

    def __str__(self):
        return self.specalistion

# TODO: Add comment model here or in a new app "Blog" (maybe?)
