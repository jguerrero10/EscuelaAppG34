from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .forms import ProfesorForm
from .models import *

def list_profesor(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesor/list_profesor.html', {'profesores': profesores})

def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = form.save()
            mensaje = f'El Profesor {profesor} fue agregado correctamente'
        else:
            mensaje = f'El Profesor {profesor} no fue agregado'
        return render(request, 'profesor/mensaje.html', {'mensaje': mensaje})
    else:
        form = ProfesorForm()
        return render(request, 'profesor/crear_profesor.html', {'form': form})
    
def actualizar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            profesor = form.save()
            mensaje = f'El Profesor {profesor} fue actualizado correctamente'
        else:
            mensaje = f'El Profesor {profesor} no fue actualizado'
        return render(request, 'profesor/mensaje.html', {'mensaje': mensaje})
    else:
        form = ProfesorForm(instance=profesor)
        return render(request, 'profesor/crear_profesor.html', {'form': form})
    
def eliminar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    mensaje = f'El Profesor {profesor} fue eliminado correctamente'
    return render(request, 'profesor/mensaje.html', {'mensaje': mensaje})
