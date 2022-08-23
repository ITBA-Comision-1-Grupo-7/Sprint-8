from django.db import models
from django.contrib.auth.models import User




class TipoCliente(models.Model):
    customer_type_id = models.AutoField(primary_key=True)
    customer_description = models.TextField()

    class Meta:
        db_table = 'tipo_cliente'

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_DNI = models.TextField(db_column='customer_DNI', unique=True)  # Field name made lowercase.
    dob = models.TextField()
    branch_id = models.IntegerField()


    class Meta:
        db_table = 'cliente'
        
