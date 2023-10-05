from django.urls import path
from  AppCoder  import views
      
urlpatterns = [
    path('inicio/', views.inicio),
    path('cursos/', views.cursos, name="Cursos"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('profesores/', views.profesores, name="Profesores")
    
     ]
