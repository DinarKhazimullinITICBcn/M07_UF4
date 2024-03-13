from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render

def index(request):
    professor = {"name":"Roger","surname":"Sobrino","age":"17"}
    return render(request, 'index_centre.html', {'nombre':professor['name'], 'surname':professor['surname'], 'age':professor["age"]})
def teachers(request):
    professors = [
        {    
            "id": 1,
            "nom":"Roger",
            "cognom":"Sobrino",
            "correu":"roger.sobrino@iticbcn.cat",
            "curs":"DAM2B,DAW2A",
            "moduls":"M7 Desenvolupament web d'entorn servidor"
        },
        {    
            "id": 2,
            "nom":"Josep Oriol",
            "cognom":"Roca",
            "correu":"oriol.roca@iticbcn.cat",
            "curs":"DAM2B,DAW2A, DAW1A",
            "moduls":"M9 Accessibilitat i usabilitat, M6 Desenvolupament web en entorn client"
        },
        {    
            "id": 3,
            "nom":"Juanma",
            "cognom":"Biel",
            "correu":"juanma.sanchez@iticbcn.cat",
            "curs":"DAW2A",
            "moduls":"M6 Desenvolupament web en entorn client"
        },
    ]
    context = {'professor':professors}
    return render(request, 'prof.html', context)
def students(request):
    alumnes = [
        {    
            "id": 1,
            "nom":"Dinar",
            "cognom":"Khazimullin",
            "correu": 39,
            "curs":"teacher",
            "rol":"DAM2B,DAW2A"
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
