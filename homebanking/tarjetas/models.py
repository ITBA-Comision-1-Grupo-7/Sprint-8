from django.db import models
from clientes.models import Cliente

# Create your models here.

class Tarjetas(models.Model):
  name= models.CharField(max_length=100)
  email= models.EmailField()
  tarjeta = models.CharField(max_length=100)
  def __str__(self): 
    return self.name


class MarcaTarjeta(models.Model):
    marca_tarjeta_id = models.AutoField(primary_key=True)
    marca_name = models.TextField()

    class Meta:
        db_table = 'marca_tarjeta'


class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.TextField(unique=True)
    card_expire_date = models.DateField()
    card_cvv = models.TextField(db_column='CVV')  # Field name made lowercase.
    card_type = models.TextField()
    account_id = models.IntegerField()
    cardbrand_id = models.ForeignKey(MarcaTarjeta, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tarjeta'