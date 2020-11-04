from django.db import models

# Create your models here.


class Usuario(models.Model):

    ROLES = (
        ('Comisión', 'comision'),
        ('Investigador', 'investigador'),
        ('Estudiante investigador', 'estudiante_investigador')
    )

    nombre = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    rol = models.CharField(max_length=50, null=True, choices=ROLES)

    def __str__(self):
        return self.nombre
