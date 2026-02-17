from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h2>Информация о лыжах</h2>")


def catalog(request, id):
    return HttpResponse(f"Некий каталог {id}.")