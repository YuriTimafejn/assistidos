from django.shortcuts import render

def index(request):
    return render(request, 'galeria/index.html')

def registro(request):
    return render(request, 'galeria/filme_serie.html')