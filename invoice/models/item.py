import decimal
from django.db import models



class Item(models.Model):
    invoice = models.ForeignKey("invoice.Invoice", related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    net_amount = models.DecimalField(max_digits=6, decimal_places=2)
    vat_rate = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)

    def get_gross_amount(self):
        vat_rate = decimal.Decimal(self.vat_rate/100)
        return self.net_amount + (self.net_amount * vat_rate)