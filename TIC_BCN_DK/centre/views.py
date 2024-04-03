from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm

def index(request):
    professor = {"name":"Roger","surname":"Sobrino","age":"17"}
    return render(request, 'index_centre.html', {'nombre':professor['name'], 'surname':professor['surname'], 'age':professor["age"]})
def teachers(request):
    professors = Persona.objects.filter(rol='professor')
    context = {'professor':professors}
    return render(request, 'prof.html', context)
def students(request):
    alumnes = Persona.objects.filter(rol='alumne')
    context = {'alumne':alumnes}
    return render(request, 'alumne.html', context)
def teacher(request, pk):
    professor = Persona.objects.get(id=pk)
    return render(request, 'professor.html', {'professor': professor})
def student(request, pk):
    alumne = Persona.objects.get(id=pk)
    return render(request, 'alumn.html', {'alumne': alumne})
def form(request):
    form = PersonaForm()
    context = {'form':form}
    return render(request, 'form.html', context)