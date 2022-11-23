from django.shortcuts import render
from .models import Curso

def home(request):
    cursos = Curso.objects.all()
    return  render(request,'gestionCursos.html', {"cursos": cursos})