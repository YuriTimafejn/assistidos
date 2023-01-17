from django.urls import path
from galeria.views import index, registro

urlpatterns = [
    path('', index, name='listagem_producoes'),
    path('producao/', registro, name='producao'),
]