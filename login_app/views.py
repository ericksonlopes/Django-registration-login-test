from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout


def login(request: HttpRequest):
    # se for apenas GET
    if request.method == 'GET':
        return render(request, 'seu_login/login.html')

    # se for outra requisição ou POST / POST esta com todas as informações passada pelo form
    username = request.POST.get('username')  # retorna none se nada for encontrado
    password = request.POST.get('password')

    # retorna o usuario encontrado
    user = authenticate(username=username, password=password)

    # se entrar dentro do if as credenciais são validas
    if user:
        # login apenas / autenticando no sistema
        django_login(request, user)
        # retorna página home
        return redirect('/home/')

    # caso não seja autenticado
    return render(request, 'seu_login/login.html', {'message': 'Credenciais invalidas'})


def logout(request):
    django_logout(request)
    return redirect('/')


def register(request):
    if request.method == 'GET':
        return render(request, 'seu_login/register.html')


@login_required(login_url='/login/')
def home(request):
    return render(request, 'seu_login/home.html')
