import bcrypt
from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from .models import Houses, Wizards, Users


def index(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)


def register(request):

    if request.method == 'GET':
        return render(request, 'register.html')

    else:
        # si llega por un POST, tomar valores del formulario
        # y crear un nuevo usuario
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # validar que el formulario esté correcto
        errors = Users.objects.basic_validator(request.POST)
        if len(errors) > 0:
            # en este caso, hay al menos 1 error en el formulario
            # voy a mostrarle los errores al usuario
            for llave, mensaje_de_error in errors.items():
                messages.error(request, mensaje_de_error)
        
            return redirect('/register')
        
        # si llegamos hasta acá, estamos seguros que ambas coinciden
        user = Users.objects.create(
            name=name,
            email=email,
            password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        )
        request.session['user'] = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'avatar': user.avatar
        }
        messages.success(request, 'Usuario creado con éxito')
        return redirect('/shows')


def login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        user = Users.objects.get(email=email)
    except Users.DoesNotExist:
        messages.error(request, 'Usuario inexistente o contraseña incorrecta')
        return redirect('/register')
    
    # si llegamos acá, estamos seguros que al  menos el usuario SI existe
    if  not bcrypt.checkpw(password.encode(), user.password.encode()): 
        messages.error(request, 'Usuario inexistente o contraseña incorrecta')
        return redirect('/register')
    
    # si llegamos hasta acá, estamos seguros que es el usuario y la contraseña está correcta
    request.session['user'] = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'avatar': user.avatar
    }
    messages.success(request, f'Hola {user.name}')
    return redirect('/shows')


def logout(request):
    request.session['user'] = None
    return redirect('/register')

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


'''
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

    return redirect('/shows')
'''

from .forms import WizardForm

def new_show(request):
    # primero recupero los campos del formulario
    name = request.POST['name']
    house_id = request.POST['house_id']
    pet = request.POST['pet']
    year = request.POST['year']

    # luego valido que estos campos sean correctos
    form = WizardForm(request.POST)
    if not form.is_valid():
        for llave, valor in form.errors.items():
            messages.error(request, f'{llave}: {valor[0]}')
        return redirect('/shows/create')

    # si llego acá, entonces el formulario está todo OK
    wizard = Wizards.objects.create(name=name, house_id=int(house_id),
                                    pet=pet, year=year)
                                    
    messages.success(request, f'El mago {name} ha sido agregado')

    return redirect('/shows')



def show(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'show.html', context)


