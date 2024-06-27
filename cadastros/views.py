from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Exame
from .forms import ClienteForm, ExameForm
from django.db.models import Sum, Q, F, DecimalField
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'cadastros/home.html')


@login_required
def cliente_list(request):
    termo_pesquisa = request.GET.get('q','')

    clientes = Cliente.objects.filter(
        Q(nome__icontains = termo_pesquisa) |
        Q(cpf__icontains = termo_pesquisa) 
        
    )
    return render(request, 'cadastros/cliente_list.html', {'clientes': clientes, 'termo_pesquisa': termo_pesquisa})



@login_required
def cliente_detail(request, id):
    clientes = get_object_or_404(Cliente, id=id)
    return render(request, 'cadastros/cliente_detail.html', {'clientes': clientes})

@login_required
def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST, request.FILES)     #adicionando foto
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'cadastros/cliente_form.html', {'form': form})


@login_required
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


@login_required
def cliente_delete(request, id):
    clientes = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        clientes.delete()
        return redirect('cliente_list')
    return render(request, 'cadastros/cliente_confirm_delete.html', {'clientes':clientes})


@login_required
def exame_datail(request, id):
    exames = get_object_or_404(Exame, id=id)
    return render(request, 'cadastros/exame_detail.html', {'exames': exames})


@login_required
def exame_list_all(request):
    exames = Exame.objects.all()
    return render(request, 'cadastros/exame_list_all.html', {'exames': exames})



@login_required
def exame_list(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    exames = Exame.objects.filter(cliente=cliente)
    total_preco = exames.aggregate(total=Sum(F('preco'), output_field=DecimalField(decimal_places=2, max_digits=10)))['total'] or 0.00
    #arredonda o valor
    total_preco = round(total_preco, 2)
    return render(request, 'cadastros/exame_list.html', {'exames': exames, 'cliente': cliente, 'total_preco': total_preco})

@login_required
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


@login_required
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


@login_required
def exame_delete(request, cliente_id, id):
    exame = get_object_or_404(Exame, id=id, cliente_id=cliente_id)
    if request.method == "POST":
        exame.delete()
        return redirect('exame_list', id=cliente_id)
    return render(request, 'cadastros/exame_confirm_delete.html', {'exame': exame})
