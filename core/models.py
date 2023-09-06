from django.db import models
from datetime import date

# Create your models here.
class Information(models.Model):
    date = models.DateField(('date'), default= date.today)
    trade_code = models.CharField(max_length=50)
    high = models.CharField(max_length=300)
    low = models.CharField(max_length=300)
    open = models.CharField(max_length=300)
    close = models.CharField(max_length=300)
    volume = models.CharField(max_length=300)
    
    def __str__(self):
        return str(self.date)
    
