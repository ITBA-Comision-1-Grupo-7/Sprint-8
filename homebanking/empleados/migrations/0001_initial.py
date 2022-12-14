# Generated by Django 4.1 on 2022-08-25 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Empleado",
            fields=[ 
                ("employee_id", models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
                ("employee_name", models.TextField()),
                ("employee_surname", models.TextField()),
                ("employee_hire_date", models.TextField()),
                ("employee_dni", models.TextField(db_column="employee_DNI")),
                ("branch_id", models.IntegerField()),
            ],
            options={"db_table": "empleado"},
        ),
    ]
