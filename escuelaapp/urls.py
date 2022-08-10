from django.urls import path
from .views import *

urlpatterns = [
    path('listar/profesor/', list_profesor),
    path('crear/profesor/', crear_profesor),
    path('actualizar/profesor/<int:id>', actualizar_profesor),
    path('eliminar/profesor/<int:id>', eliminar_profesor)
]