from django.db import models

# Create your models here.
class Prestamos(models.Model):
  apellido = models.CharField(max_length=20)
  fecha_inicio = models.DateField()
  valor = models.IntegerField()
  dni = models.CharField(max_length=9) 
  PRESTAMO_PERSONAL = "PP"
  PRESTAMO_ESTUDIANTE = "PE"
  PRESTAMO_COMERCIOS = "PC"
  PRESTAMO_HIPOTECARIO= "PH"
  TIPO_PRESTAMO = [
    (PRESTAMO_PERSONAL,"Prestamo_personal"),
    (PRESTAMO_ESTUDIANTE,"Prestamo_estudiante"),
    (PRESTAMO_COMERCIOS,"Prestamo_comercios"),
    (PRESTAMO_HIPOTECARIO, "Prestamo_hipotecario"),
] 
  tipo_prestamo = models.CharField(max_length=2, choices=TIPO_PRESTAMO, default = PRESTAMO_PERSONAL)
  estado_prestamo = models.BooleanField(default=True)


