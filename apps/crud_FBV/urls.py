from django.urls import path
from . import views

urlpatterns = [
    path('fbv/', views.listar_cosas, name='listar_cosas'),
    path('fbv/crear/', views.crear_cosa, name='crear_cosa'),
    path('fbv/editar/<int:id>/', views.editar_cosa, name='editar_cosa'),
    path('fbv/eliminar/<int:id>/', views.eliminar_cosa, name='eliminar_cosa'),
]
