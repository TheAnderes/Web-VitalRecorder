# vital_recorder/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                 # /
    path('sobre/', views.about, name='sobre'),         # /sobre/
    path('producto/', views.product, name='producto'), # /producto/
    path('contacto/', views.contact, name='contacto'), # /contacto/
]
