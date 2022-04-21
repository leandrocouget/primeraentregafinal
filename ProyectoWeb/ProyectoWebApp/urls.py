from django.urls import path
from ProyectoWebApp import views



urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('blog', views.blog, name = "blog"),
    path('buscador', views.buscador, name = "buscador"),
    path('contacto', views.contacto, name = "contacto"),
    path('base', views.base, name = "base"),
    path('formulario', views.formulario, name = "formulario"),
    path('ingreso', views.ingreso, name = "ingreso"),
    path('buscar/', views.buscar),
]