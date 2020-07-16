from django.shortcuts import render

def register_user(request):
    if request.method == "POST":
        form_user = UserCreationForm(request.POst)
