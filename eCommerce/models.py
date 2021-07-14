from django.db import models
from directory.models import Artist, Customer


class Purchase(models.Model):
    pur_date = models.DateTimeField('Purchase Date')
    cost = models.DecimalField('Total Cost', max_digits=10, decimal_places=2)
    seller = models.ForeignKey(Artist, on_delete=models.RESTRICT)
    buyer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    # TODO: Add Payment method

    def __str__(self):
        return self.pur_date

    # TODO: Add Invoice (maybe?)

# TODO: Add Payment detail model
