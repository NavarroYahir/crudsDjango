from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from apps.crud_ninja.models import Cosa
from .forms import CosaForm


class ListaCosasView(ListView):
    model = Cosa
    template_name = 'lista.html'
    context_object_name = 'cosas'


class CrearCosaView(CreateView):
    model = Cosa
    form_class = CosaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('listar_cosas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Cosa'
        return context


class EditarCosaView(UpdateView):
    model = Cosa
    form_class = CosaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('listar_cosas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cosa'
        return context


class EliminarCosaView(DeleteView):
    model = Cosa
    template_name = 'eliminar.html'
    success_url = reverse_lazy('listar_cosas')

def main_view(request):
    return render(request, 'main.html')