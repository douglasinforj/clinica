from django import forms
from .models import Cliente, Exame

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone', 'email', 'data_nascimento']

class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ['tipo_exame', 'data_exame', 'resultado', 'preco']