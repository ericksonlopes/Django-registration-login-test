from django.shortcuts import render


def login(request):
    return render(request, 'seu_login/login.html')
