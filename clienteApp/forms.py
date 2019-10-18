from django import forms
from django.forms import ModelForm, forms
from django.contrib.auth.forms import UserCreationForm

from .models import Cliente, Usuario

''''classe para importar'''

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['cep', 'nome', 'endereco', 'numero', 'cidade', 'estado', 'pais', 'telefone']

class CadastroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email']
        help_texts = {
            'username': None,
        }
