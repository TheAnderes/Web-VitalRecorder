# vital_recorder/views.py
from django.shortcuts import render

def home(request):
    return render(request, "home/index.html")   # ✅ carpeta home

def sobre(request):
    return render(request, "pages/sobre.html")     # ✅ MUÉVELO fuera de partials

def producto(request):
    return render(request, "pages/producto.html")  # si aún no existe, créalo

def contacto(request):
    return render(request, "pages/contacto.html")  # si aún no existe, créalo
