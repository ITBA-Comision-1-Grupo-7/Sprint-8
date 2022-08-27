from operator import truediv
from django.db import models

# Create your models here.
class Sucursal(models.Model):
    branch_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='branch_id')
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sucursal'

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)  # This field type is a guess.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.TextField()
    card_expire = models.TextField()
    card_expire_date = models.TextField()
    card_cvv = models.TextField()
    card_type = models.TextField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarjeta'

class Direccion(models.Model):
    branch_id = models.AutoField(unique=True, primary_key=True)
    address_id = models.IntegerField()
    address_text = models.TextField()
    posta_zip = models.TextField()
    city = models.TextField()
    state = models.TextField()
    country = models.IntegerField()
    customer_id = models.IntegerField()
    employee_id = models.IntegerField()
    sucursar_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'direccion'

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'