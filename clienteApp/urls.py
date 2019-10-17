from django.urls import path
from .views import clienteList, clienteCreate, clienteUpdate, clienteDelete


urlpatterns = [
    path('list/', clienteList, name='clienteList'),
    path('create/', clienteCreate, name='clienteCreate'),
    path('update/<int:id>/', clienteUpdate, name='clienteUpdate'),
    path('delete/<int:id>/', clienteDelete, name='clienteDelete'),



]