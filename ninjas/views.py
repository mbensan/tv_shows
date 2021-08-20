from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Ninjas

def index(request):
    context = {
        'saludo': 'Hola dsde Ninjas'
    }
    return render(request, 'index.html', context)


def create(request):
    # print(request.POST)
    ninja = Ninjas.objects.create(
        name=request.POST['name'],
        color=request.POST['color']
    )

    return JsonResponse({
        'id': ninja.id,
        'name': ninja.name,
        'color': ninja.color
    })

def all(request):
    ninjas = Ninjas.objects.all()
    ninjas = [{
        'id': ninja.id,
        'name': ninja.name,
        'color': ninja.color
    } for ninja in ninjas]

    return JsonResponse({'ninjas': ninjas})

#show.release_date.strftime('%Y-%m-%d')

