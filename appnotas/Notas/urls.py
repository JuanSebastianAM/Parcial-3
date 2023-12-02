from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.NotasIndex, name='NotasIndex'),
    path('gestion/',views.gestionNotas, name='gestionNotas'),
    path('crear/',views.crearNotas, name='crearNotas'),
    path('detalle/<id>/',views.detalleNotas, name='detalleNotas'),
    path('editar/<id>/',views.editarNotas, name='editarNotas'),
    path('borrar/<id>/',views.eliminarNotas, name='eliminarNotas'),
    path('ver/<id>/',views.verNotas, name='verNotas')
]