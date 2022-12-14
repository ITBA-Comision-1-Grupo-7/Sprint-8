# Generated by Django 4.0.6 on 2022-08-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=20)),
                ('fecha_inicio', models.DateField()),
                ('valor', models.IntegerField()),
                ('dni', models.CharField(max_length=9)),
                ('tipo_prestamo', models.CharField(choices=[('PP', 'Prestamo_personal'), ('PE', 'Prestamo_estudiante'), ('PC', 'Prestamo_comercios'), ('PH', 'Prestamo_hipotecario')], default='PP', max_length=2)),
                ('estado_prestamo', models.BooleanField(default=True)),
            ],
        ),
    ]
