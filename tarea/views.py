from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from tarea.models import Tarea


def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tarea/lista_tareas.html', {'tareas': tareas})


def detalle_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, 'tarea/detalle_tarea.html', {'tarea': tarea})


def crear_tarea(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        completado = True if request.POST.get('completado') == 'on' else False
        Tarea.objects.create(titulo=titulo, descripcion=descripcion, completado=completado)

        return redirect(reverse('tarea:lista_tareas'))

    return render(request, 'tarea/tarea_form.html')


def modificar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        completado = True if request.POST.get('completado') == 'on' else False
        tarea.titulo = titulo
        tarea.descripcion = descripcion
        tarea.completado = completado
        tarea.save()

        return redirect(reverse('tarea:lista_tareas'))

    return render(request, 'tarea/tarea_form.html', {'tarea': tarea})


def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.delete()
        return redirect(reverse('tarea:lista_tareas'))

    return render(request, 'tarea/tarea_confirm_delete.html', {'tarea': tarea})
