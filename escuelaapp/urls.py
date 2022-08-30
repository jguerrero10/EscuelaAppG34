from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('listar/profesor/', list_profesor, name='lista-profesor'),
    path('crear/profesor/', crear_profesor, name='crear-profesor'),
    path('actualizar/profesor/<int:id>', actualizar_profesor, name='actualizar-profesor'),
    path('eliminar/profesor/<int:id>', eliminar_profesor, name='eliminar-nombre')
]