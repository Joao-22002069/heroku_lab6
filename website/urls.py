from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='Home'),
    path('Exemplos', views.exemplos_page_view, name='Exemplos'),
    path('Sobre', views.sobre_page_view, name='Sobre'),
]