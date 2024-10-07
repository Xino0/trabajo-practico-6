from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_horas = models.IntegerField()

    def __str__(self):
        return str(self.nombre)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    nota_curso = models.DecimalField(max_digits=4, decimal_places=2)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'