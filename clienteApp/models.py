from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser


class Usuario(AbstractUser):
    username = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)


    REQUIRED_FIELDS = ('email', 'password1', 'password2')

    USERNAME_FIELD = ('username')


class Cliente(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    telefone = models.CharField(max_length=10)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=6)
    cidade = models.CharField(max_length=15)
    estado = models.CharField(max_length=15)
    pais = models.CharField(max_length=15)
    cep = models.CharField(max_length=9, default='58010-000')

    def __str__(self):
        return self.nome

    '''Função para retornar pelo nome'''