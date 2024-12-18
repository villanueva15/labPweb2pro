from django.urls import path
from . import views

urlpatterns = [
    path('registro/usuario/', views.registro_usuario, name='registro_usuario'),
    path('registro/libro/', views.registro_libro, name='registro_libro'),
    path('registro/review/', views.registro_review, name='registro_review'),
    path('registro/exitoso/', views.registro_exitoso, name='registro_exitoso'),  # Esta es la página de éxito
    path('registro/exitoso/libro/', views.registro_exitoso_libro, name='registro_exitoso_libro'),
    path('registro/exitoso/review/', views.registro_exitoso_review, name='registro_exitoso_review'),
]

