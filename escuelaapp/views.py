from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .forms import *
from django.contrib.auth.models import Permission, User, Group
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    return render(request, 'home/index.html')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
            else:
                form = LoginForm()
                messages.add_message(request, messages.ERROR, 'Las credenciales no son correctas')
                return render(request, 'acceso/login.html', {'form': form}) 
        else:
            return render(request, 'acceso/login.html')
         
    else:
        form = LoginForm()
        return render(request, 'acceso/login.html', {'form': form})

@login_required    
def logout_user(request):
    logout(request)
    return redirect(reverse('home'))
    
@login_required(login_url='/login/')    
def listar_rol(request):
    roles = Group.objects.all()
    return render(request, 'roles/index.html', {'roles': roles})

@login_required(login_url='/login/') 
def crear_rol(request):
    if request.method == 'POST':
        form = GroupsForm(request.POST)
        if form.is_valid():
            grupo = form.save()
            permisos = form.cleaned_data['permisos']    
            grupo.permissions.set(permisos)
            messages.success(request, "Rol almacenado correctamente")     
        else:
            messages.error(request, "Error al crear rol")
        return redirect(reverse('listar-rol'))
    else:
        form = GroupsForm()
        return render(request, 'roles/rolform.html', {'form': form})

@login_required(login_url='/login/')     
def eliminar_rol(request, id):
    rol = Group.objects.get(id=id)
    rol.delete()
    mensaje = f'El Rol {rol.name} fue eliminado correctamente'
    return render(request, 'layout/mensaje.html', {'mensaje': mensaje})

@login_required(login_url='/login/') 
def agregar_permisos(request):
    if request.method == 'POST':
        permisos = request.POST.getlist('permisos')
        rol = Group.objects.get(id = request.POST.get('rol'))
        rol.permissions.set(permisos)
        return HttpResponse("Hecho")

@login_required(login_url='/login/') 
def list_profesor(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesor/list_profesor.html', {'profesores': profesores})

@login_required(login_url='/login/') 
def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            nombres = form.cleaned_data['nombres']
            apellidos = form.cleaned_data['apellidos']
            rol = form.cleaned_data['rol']
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=nombres,
                last_name= apellidos,
            )
            user.groups.add(rol)
            profesor = form.save(commit=False)
            profesor.user = user
            profesor.save()
            mensaje = f'El Profesor {profesor} fue agregado correctamente'
        else:
            mensaje = f'El Profesor {profesor} no fue agregado'
        return render(request, 'layout/mensaje.html', {'mensaje': mensaje})
    else:
        form = ProfesorForm()
        return render(request, 'profesor/crear_profesor.html', {'form': form})

@login_required(login_url='/login/')    
def actualizar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            profesor = form.save()
            mensaje = f'El Profesor {profesor} fue actualizado correctamente'
        else:
            mensaje = f'El Profesor {profesor} no fue actualizado'
        return render(request, 'layout/mensaje.html', {'mensaje': mensaje})
    else:
        form = ProfesorForm(instance=profesor)
        return render(request, 'profesor/crear_profesor.html', {'form': form})

@login_required(login_url='/login/')  
def eliminar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    mensaje = f'El Profesor {profesor} fue eliminado correctamente'
    return render(request, 'profesor/mensaje.html', {'mensaje': mensaje})

@login_required(login_url='/login/')
def listar_programa(request):
    programas = Programa.objects.all() # select * from escuelapp_programa
    return render(request, 'programa/listar_programa.html', {'programas': programas})

@login_required(login_url='/login/')
def crear_programa(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Los datos del programa fueron almacenados correctamente") 
        else:
            messages.error(request, "Verifique los datos e intente nuevamente") 
        return redirect(reverse('listar-programa'))
    else:
        form = ProgramaForm()
        contexto = {
            'form': form,
            'accion': 'Crear'
            }
        return render(request, 'programa/crear_actualizar_programa.html', contexto)
    
@login_required
def actualizar_programa(request, id):
    programa = Programa.objects.get(id=id)
    if request.method == 'POST':
        form = ProgramaForm(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            messages.success(request, "Los datos del programa fueron actualizados correctamente") 
        else:
            messages.error(request, "Verifique los datos e intente nuevamente")
        return redirect(reverse('listar-programa')) 
    else:
        form = ProgramaForm(instance=programa)
        contexto = {
            'form': form,
            'accion': 'Actualizar'
            }
        return render(request, 'programa/crear_actualizar_programa.html', contexto)
    
@login_required
def eliminar_programa(request, id):
    try:
        programa = Programa.objects.get(id=id)
        programa.delete()
        messages.success(request, "Los datos del programa fueron eliminados correctamente") 
    except ObjectDoesNotExist:
        messages.error(request, "El programa no existe en la base de datos")
    return redirect(reverse('listar-programa')) 

    