from django.shortcuts import render

def index(request):
    return render (request, "Personal/principal.html")

def buscar(request):
    return render(request, 'Personal/principal.html')