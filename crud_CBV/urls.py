from django.urls import path
from .views import ListaCosasView, CrearCosaView, EditarCosaView, EliminarCosaView, main_view

urlpatterns = [
    path('', main_view, name='main'),
    path('cbv/', ListaCosasView.as_view(), name='listar_cosas'),
    path('cbv/crear/', CrearCosaView.as_view(), name='crear_cosa'),
    path('cbv/editar/<int:pk>/', EditarCosaView.as_view(), name='editar_cosa'),
    path('cbv/eliminar/<int:pk>/', EliminarCosaView.as_view(), name='eliminar_cosa'),
]
