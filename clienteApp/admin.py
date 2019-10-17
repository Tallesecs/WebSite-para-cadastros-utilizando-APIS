from django.contrib import admin

from .models import Cliente
from .models import Usuario

admin.site.register(Cliente)
admin.site.register(Usuario)
