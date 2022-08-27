# Generated by Django 4.0.6 on 2022-08-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI')),
                ('dob', models.TextField(blank=True, null=True)),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('address_id', models.IntegerField()),
                ('address_text', models.TextField()),
                ('posta_zip', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('country', models.IntegerField()),
                ('customer_id', models.IntegerField()),
                ('employee_id', models.IntegerField()),
                ('sucursar_id', models.IntegerField()),
            ],
            options={
                'db_table': 'direccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.TextField()),
                ('employee_surname', models.TextField()),
                ('employee_hire_date', models.TextField()),
                ('employee_dni', models.TextField(db_column='employee_DNI')),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('card_id', models.AutoField(primary_key=True, serialize=False)),
                ('card_number', models.TextField()),
                ('card_expire', models.TextField()),
                ('card_expire_date', models.TextField()),
                ('card_cvv', models.TextField()),
                ('card_type', models.TextField()),
                ('customer_id', models.IntegerField()),
            ],
            options={
                'db_table': 'tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='branch_id')),
                ('branch_number', models.BinaryField()),
                ('branch_name', models.TextField()),
                ('branch_address_id', models.IntegerField()),
            ],
            options={
                'db_table': 'sucursal',
                'managed': True,
            },
        ),
    ]
