from django.db import models

# Create your models here.

class Books(models.Model):
    BookId = models.AutoField(primary_key=True)
    BookName = models.CharField(max_length=500)
    Quantity = models.BigIntegerField()
    BookGenre = models.CharField(max_length=500)
    IsBestSeller = models.BooleanField(max_length=500)
    CreatedAt = models.DateField()
    UpdatedAt = models.DateField()
