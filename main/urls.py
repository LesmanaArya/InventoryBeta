from django.urls import path
from . import views

#URL Config
urlpatterns = [
    path('', views.home), #Jika url main nya berupa string kosong, jalankan fungsi home yang ada di views.py
]