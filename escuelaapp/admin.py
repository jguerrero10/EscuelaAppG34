import site
from django.contrib import admin
from escuelaapp.models import *

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Programa)
admin.site.register(Materia)
admin.site.register(Seguimiento)
