from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from .models import Houses, Wizards

def index(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)


def shows(request):
    wizards = Wizards.objects.all()
    context = {
        'wizards': wizards
    }
    return render(request, 'shows.html', context)


def create(request):
    houses = Houses.objects.all()

    context = {
        'houses': houses
    }
    return render(request, 'create.html', context)


def edit(request, id):
    if request.method == 'GET':
        houses = Houses.objects.all()
        wizard = Wizards.objects.get(id=id)

        context = {
            'houses': houses,
            'wizard': wizard
        }
        return render(request, 'edit.html', context)
    
    else: # en este caso el formulario vino con cosas
        wizard = Wizards.objects.get(id=id)
        wizard.name = request.POST['name']
        wizard.pet = request.POST['pet']
        # .... cambiamos todas las cosas

        wizard.save()
        messages.success('Cambiamos un mago')

        return redirect('/shows')
         


def destroy(request, id):
    wizard = Wizards.objects.get(id=id)
    wizard.delete()
    return redirect('/shows')


def new_show(request):
    # primero recupero los campos del formulario
    name = request.POST['name']
    house_id = request.POST['house_id']
    pet = request.POST['pet']
    year = request.POST['year']

    # luego valido que estos campos sean correctos
    errors = Wizards.objects.basic_validator(request.POST)

    if len(errors) > 0:
        # en este caso, hay al menos 1 error en el formulario
        # voy a mostrarle los errores al usuario
        for llave, mensaje_de_error in errors.items():
            messages.error(request, mensaje_de_error)
        
        return redirect('/shows/create')

    # si llego acá, entonces el formulario está todo OK
    wizard = Wizards.objects.create(name=name, house_id=int(house_id),
                                    pet=pet, year=year)
                                    
    messages.success(request, f'El mago {name} ha sido agregado')
    #messages.error(request, 'Ojalá no le pase nada malo')
    #messages.warning(request, f'Su mascota se llama {pet}')
    return redirect('/shows')
    



def show(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'show.html', context)


