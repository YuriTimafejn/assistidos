from django.urls import path
from galeria.views import index, registro

urlpatterns = [
    path('', index),
    path('produção/', registro)
]