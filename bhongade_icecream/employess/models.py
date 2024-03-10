from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    mobile_no = models.BigIntegerField()
    address = models.CharField(max_length=150)
    total = models.FloatField()
    paid = models.FloatField()
    balance = models.FloatField()

    class Meta:
        db_table = 'EMPLOYEE_MASTER'

    def __str__(self):
        return f'''{self.__dict__}'''
    
    def __repr__(self):
        return str(self)
 
