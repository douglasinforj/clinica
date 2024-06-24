from django.db import models

class Cliente(models.Model):
    foto = models.ImageField(upload_to='static/fotos_clientes/')
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Exame(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_exame = models.CharField(max_length=100)
    data_exame = models.DateField()
    resultado = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tipo_exame} - {self.cliente.nome}"