from django.db import models

class Cliente(models.Model):
    nome = models.models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome
