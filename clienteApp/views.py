from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm, CadastroForm
from django.contrib.auth.decorators import login_required
import requests

def home(request):
    response = requests.get('viacep.com.br/ws/%s/json')
    print(response)



def usuarioCreate(request):
    form = CadastroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('clienteList')

    return render(request, 'registration/cadastro.html', {'form': form})

'''Importando login required para pedir login
 quem entrar como admin vai poder ver.
 '''

@login_required
def clienteList(request):
    clientes = Cliente.objects.all()

    return render(request, 'clienteList.html', {'clientes': clientes})


@login_required
def clienteCreate(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('clienteList')

    return render(request, 'clienteCreate.html', {'form': form})


@login_required
def clienteUpdate(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('clienteList')

    return render(request, 'clienteCreate.html', {'form': form})


@login_required
def clienteDelete(request, id):
    cliente = get_object_or_404(Cliente, pk=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('clienteList')

    return render(request, 'clienteDelete.html', {'cliente': cliente})

@login_required
def clienteRead(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    return render(request, 'clienteRead.html', {'cliente': cliente, 'form': form})



'''Função de cadastro'''

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CadastroForm()
    return render(request, 'registration/cadastro.html', {'form': form})

