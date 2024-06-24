from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Exame
from .forms import ClienteForm, ExameForm
from django.db.models import Sum

def home(request):
    return render(request, 'cadastros/home.html')

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cadastros/cliente_list.html', {'clientes': clientes})


def cliente_detail(request, id):
    clientes = get_object_or_404(Cliente, id=id)
    return render(request, 'cadastros/cliente_detail.html', {'cliente': clientes})


def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST, request.FILES)     #adicionando foto
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'cadastros/cliente_form.html', {'form': form})

def cliente_update(request, id):
    clientes = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=clientes)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=clientes)
    return render(request, 'cadastros/cliente_form.html', {'form': form})

def cliente_delete(request, id):
    clientes = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        clientes.delete()
        return redirect('cliente_list')
    return render(request, 'cadastros/cliente_confirm_delete.html', {'cliente':clientes})

def exame_list(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    exames = Exame.objects.filter(cliente=cliente)
    total_preco = exames.aggregate(Sum('preco'))['preco__sum'] or 0.00  # Calculando o total dos preços
    return render(request, 'cadastros/exame_list.html', {'exames': exames, 'cliente': cliente, 'total_preco': total_preco})
          
def exame_create(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        form = ExameForm(request.POST)
        if form.is_valid():
            exame = form.save(commit=False)
            exame.cliente = cliente
            exame.save()
            return redirect('exame_list', id=cliente.id)
    else:
        form = ExameForm()
    return render(request, 'cadastros/exame_form.html', {'form': form, 'cliente': cliente})  

def exame_update(request, cliente_id, id):
    exame = get_object_or_404(Exame, id=id, cliente_id=cliente_id)
    if request.method == "POST":
        form = ExameForm(request.POST, instance=exame)
        if form.is_valid():
            form.save()
            return redirect('exame_list', id=cliente_id)
    else:
        form = ExameForm(instance=exame)
    return render(request, 'cadastros/exame_form.html', {'form': form, 'cliente': exame.cliente})

def exame_delete(request, cliente_id, id):
    exame = get_object_or_404(Exame, id=id, cliente_id=cliente_id)
    if request.method == "POST":
        exame.delete()
        return redirect('exame_list', id=cliente_id)
    return render(request, 'cadastros/exame_confirm_delete.html', {'exame': exame})
