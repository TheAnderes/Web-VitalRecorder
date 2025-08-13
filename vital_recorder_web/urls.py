# vital_recorder_web/urls.py
from django.contrib import admin
from django.urls import path
from vital_recorder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('producto/', views.producto, name='producto'),
    path('contacto/', views.contacto, name='contacto'),
]
