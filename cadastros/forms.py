from django import forms
from .models import Cliente, Exame

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.TextInput(attrs={'class': 'form-control'}),
            # Pode definir classes CSS para os campos aqui
        }

class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),        #ajusta para selecionar usuários cadastrados
            'tipo_exame': forms.TextInput(attrs={'class': 'form-control'}),
            'data_exame': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            'resultado': forms.Textarea(attrs={'class': 'form-control'}),
            'preco': forms.TextInput(attrs={'class': 'form-control'}),
            # Pode definir classes CSS para os campos aqui
        }