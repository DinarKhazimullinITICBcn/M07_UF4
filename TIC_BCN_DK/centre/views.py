from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render

def index(request):
    professor = {"name":"Roger","surname":"Sobrino","age":"17"}
    return render(request, 'index_centre.html', {'nombre':professor['name'], 'surname':professor['surname'], 'age':professor["age"]})
def prof(request):
    professors = [
        {    
            "id": 1,
            "nom":"Roger",
            "cognom":"Sobrino",
            "edat": 39,
            "rol":"teacher",
            "curs":"DAM2B,DAW2A"
        },
        {    
            "id": 2,
            "nom":"Josep Oriol",
            "cognom":"Roca",
            "edat":"25",
            "rol":"teacher",
            "curs":"DAM2B, DAW2A, DAW1A"
        },
        {    
            "id": 3,
            "nom":"Juanma",
            "cognom":"Biel",
            "edat":24,
            "rol":"teacher",
            "curs":"DAW2B, DAW2A"
        },
    ]
    context = {'professor':professors}
    return render(request, 'prof.html', context)
def alumne(request):
    alumnes = [
        {    
            "id": 1,
            "nom":"Dinar",
            "cognom":"Khazimullin",
            "edat": 39,
            "rol":"teacher",
            "curs":"DAM2B,DAW2A"
        },
        {    
            "id": 2,
            "nom":"Josep Oriol",
            "cognom":"Roca",
            "edat":"25",
            "rol":"teacher",
            "curs":"DAM2B, DAW2A, DAW1A"
        },
        {    
            "id": 3,
            "nom":"Juanma",
            "cognom":"Biel",
            "edat":24,
            "rol":"teacher",
            "curs":"DAW2B, DAW2A"
        },
    ]
    context = {'alumne':alumnes}
    return render(request, 'alumne.html', context)
