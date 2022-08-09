from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cod_profesor = models.CharField(max_length=12)
    direccion = models.CharField(max_length=120, blank=True)
    telefono = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Programa(models.Model):
    nombre = models.CharField(max_length=185)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
    
class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    cod_estudiante = models.CharField(max_length=12)
    direccion = models.CharField(max_length=120, blank=True)
    telefono = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Materia(models.Model):
    nombre = models.CharField(max_length=185)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
    
    
class Seguimiento(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nota = models.FloatField()
    
    def __str__(self):
        return f"{self.estudiante} - {self.nota}"
