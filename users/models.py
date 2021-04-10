from django.db import models

# Create your models here.

class StudentModels(models.Model):
    studentName= models.CharField(max_length=100)
    Hallticket = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    def __str__(self):
        return self.studentName
    class Meta:
        db_table = 'dph_student'

class ProductsModels(models.Model):
    pname = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.pname
    class Meta:
        db_table = "dph_products"