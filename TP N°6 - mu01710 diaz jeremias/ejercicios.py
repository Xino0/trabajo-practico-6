import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestor_estudiantes.settings')
django.setup()

from apps.estudiante.models import Curso, Estudiante

# Crea y guarda 2 cursos en la Base de Datos:
curso1 = Curso(nombre="Matemáticas", cantidad_horas=40)
curso2 = Curso(nombre="Historia", cantidad_horas=30)

curso1.save()
curso2.save()

# Crea y guarda al menos 3 estudiantes (junto con su curso) en la base de datos:
estudiante1 = Estudiante(nombre="Juan", apellido="Pérez", edad=19, nota_curso=8.5, curso=curso1)
estudiante2 = Estudiante(nombre="María", apellido="González", edad=22, nota_curso=9.0, curso=curso1)
estudiante3 = Estudiante(nombre="Ana", apellido="López", edad=21, nota_curso=7.5, curso=curso2)

estudiante1.save()
estudiante2.save()
estudiante3.save()

# Consulta y muestra todos los estudiantes:
todos_estudiantes = Estudiante.objects.all()
print('\nConsulta y muestra todos los estudiantes:')
for estudiante in todos_estudiantes:
    print(f'-{estudiante}')

# Consulta y muestra todos los estudiantes de un curso (por ejemplo, curso1):
estudiantes_curso1 = Estudiante.objects.filter(curso=curso1)
print('\nConsulta y muestra todos los estudiantes de un curso (por ejemplo, curso1):')
for estudiante in estudiantes_curso1:
    print(f'-{estudiante}')

# Filtra y muestra solo los estudiantes mayores de 20 años:
estudiantes_mayores_20 = Estudiante.objects.filter(edad__gt=20)
print('\nFiltra y muestra solo los estudiantes mayores de 20 años:')
for estudiante in estudiantes_mayores_20:
    print(f'-{estudiante}')

# Actualiza la nota de uno de los estudiantes:
print('\nActualiza la nota de uno de los estudiantes:')
estudiante1.nota_curso = 9.0
estudiante1.save()

# Elimina a uno de los estudiantes de la base de datos:
print('\nElimina a uno de los estudiantes de la base de datos:')
estudiante1.delete()
