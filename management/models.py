from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


USER = get_user_model()

class Fuel(models.Model):
    """Model for Fuel"""
    manager = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, related_name='user_fuels')
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=(('1', 'Active'), ('0', 'Inactive')), default=1)
    price = models.FloatField(max_length=(15, 2), default=0)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Fuel type list"

    def __str__(self):
        return f"{self.name}"

    def available(self):
        try:
            stock_in = self.stocks.aggregate(models.Sum("volume"))['volume__sum']
            if stock_in is None:
                stock_in = 0
        except:
            stock_in = 0
        try:
            sale = self.sales.aggregate(models.Sum("volume"))['volume__sum']
            if sale is None:
                sale = 0
        except:
            sale = 0
        return stock_in - sale
    


class Stock(models.Model):
    manager = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, related_name='user_stocks')
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE, related_name='stocks')
    volume = models.FloatField(max_length=(15,2), default=0)
    date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "Stock-In Records"

    def __str__(self):
        return f"{self.fuel.name} - [{self.volume} L]"
    

class Sale(models.Model):
    manager = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, related_name='user_sales')
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE, related_name='sales')
    volume = models.FloatField(max_length=(15,2), default=0)
    date = models.DateField(null=True, blank = True)
    customer_name = models.CharField(max_length=250)
    price = models.FloatField(max_length=(15,2), default=0)
    total_amount = models.FloatField(max_length=(15,2), default=0)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "List of Sales"

    def __str__(self):
        return f"{self.customer_name} - [{self.fuel} - {self.volume} L]"
