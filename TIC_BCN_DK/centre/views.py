from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from 

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
            "correu": "2023_dinar.khazimullin@iticbcn.cat",
            "curs":"DAW2A",
            "modul":"M6 Desenvolupament web en entorn client M7 Desenvolupament web en entorn servidor M8 Desplegament d'aplicacions web M9 Accessibilitat i usabilitat"
        },
        {    
            "id": 2,
            "nom":"Joel",
            "cognom":"Ghanem",
            "correu": "2023_joel.ghanem@iticbcn.cat",
            "curs":"DAW2A",
            "modul":"M6 Desenvolupament web en entorn client M7 Desenvolupament web en entorn servidor M8 Desplegament d'aplicacions web M9 Accessibilitat i usabilitat"
        },
        {    
            "id": 3,
            "nom":"Junhong",
            "cognom":"Zhu Zhang",
            "correu": "2023_junhong.zhu@iticbcn.cat",
            "curs":"DAW2A",
            "modul":"M6 Desenvolupament web en entorn client M7 Desenvolupament web en entorn servidor M8 Desplegament d'aplicacions web M9 Accessibilitat i usabilitat"
        },
    ]
    context = {'alumne':alumnes}
    return render(request, 'alumne.html', context)
def teacher(request, pk):
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
    professor = None
    for i in professors:
        if i['id'] == pk:
            professor = i
    return render(request, 'professor.html', {'professor': professor})
def student(request, pk):
    alumnes = [
        {    
            "id": 1,
            "nom":"Dinar",
            "cognom":"Khazimullin",
            "correu": "2023_dinar.khazimullin@iticbcn.cat",
            "curs":"DAW2A",
            "modul":"M6 Desenvolupament web en entorn client M7 Desenvolupament web en entorn servidor M8 Desplegament d'aplicacions web M9 Accessibilitat i usabilitat"
        },
        {    
            "id": 2,
            "nom":"Joel",
            "cognom":"Ghanem",
            "correu": "2023_joel.ghanem@iticbcn.cat",
            "curs":"DAW2A",
            "modul":"M6 Desenvolupament web en entorn client M7 Desenvolupament web en entorn servidor M8 Desplegament d'aplicacions web M9 Accessibilitat i usabilitat"
        },
        {    
            "id": 3,
            "nom":"Junhong",
            "cognom":"Zhu Zhang",
            "correu": "2023_junhong.zhu@iticbcn.cat",
            "curs":"DAW2A",
            "modul":"M6 Desenvolupament web en entorn client M7 Desenvolupament web en entorn servidor M8 Desplegament d'aplicacions web M9 Accessibilitat i usabilitat"
        },
    ]
    alumne = None
    for i in alumnes:
        if i['id'] == pk:
            alumne = i
    return render(request, 'alumn.html', {'alumne': alumne})