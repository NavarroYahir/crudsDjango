from django.shortcuts import render, redirect, get_object_or_404
from apps.crud_ninja.models import Cosa
from apps.crud_CBV.forms import CosaForm


def listar_cosas(request):
    cosas = Cosa.objects.all()
    return render(request, 'lista.html', {'cosas': cosas})


def crear_cosa(request):
    if request.method == 'POST':
        form = CosaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cosas')
    else:
        form = CosaForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Crear Cosa'})


def editar_cosa(request, id):
    cosa = get_object_or_404(Cosa, id=id)
    if request.method == 'POST':
        form = CosaForm(request.POST, instance=cosa)
        if form.is_valid():
            form.save()
            return redirect('listar_cosas')
    else:
        form = CosaForm(instance=cosa)
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Editar Cosa'})


def eliminar_cosa(request, id):
    cosa = get_object_or_404(Cosa, id=id)
    if request.method == 'POST':
        cosa.delete()
        return redirect('listar_cosas')
    return render(request, 'eliminar.html', {'cosa': cosa})
