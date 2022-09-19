from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('listar/rol/', listar_rol, name='listar-rol'),
    path('crear/rol/', crear_rol, name='crear-rol'),
    path('eliminar/rol/<int:id>', eliminar_rol, name='eliminar-rol'),
    path('listar/profesor/', list_profesor, name='lista-profesor'),
    path('crear/profesor/', crear_profesor, name='crear-profesor'),
    path('actualizar/profesor/<int:id>', actualizar_profesor, name='actualizar-profesor'),
    path('eliminar/profesor/<int:id>', eliminar_profesor, name='eliminar-nombre'),
    path('agregar/permisos/', agregar_permisos, name='agregar-permiso'),
    path('listar/programa/', listar_programa, name='listar-programa'),
    path('crear/programa/', crear_programa, name='crear-programa')
]