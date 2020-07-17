from django.contrib import admin
from django.urls import path, include
from login_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('logout/', logout),
    path('home/', home),
    path('register/', register),
    path('', home),
]
