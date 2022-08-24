from django.db import models

class Cuenta(models.Model):
    account_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    account_type_id = models.IntegerField()

    class Meta:
        db_table = 'cuenta'
