from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# Modelo customizado de usuário conforme requisitos
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True)  # tamanho maior para incluir pontos e hífen
    rg = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    
    # Endereço completo
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    
    telefone = models.CharField(max_length=20)
    foto_url = models.URLField(blank=True, null=True)  # opcional

class Token(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateField()
    data_insercao = models.DateField(auto_now_add=True)
    codigo = models.CharField(max_length=10, unique=True)  # abreviação do token
    descricao = models.TextField()
    valor_em_mangecoin = models.DecimalField(max_digits=20, decimal_places=8)
    
    def __str__(self):
        return f"{self.nome} ({self.codigo})"


class UserToken(models.Model):
    usuario = models.ForeignKey(CustomUser, related_name='tokens', on_delete=models.CASCADE)
    token = models.ForeignKey(Token, related_name='usuarios', on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=30, decimal_places=8)
    
    def __str__(self):
        return f"{self.usuario.email} - {self.token.codigo}: {self.quantidade}"


class Transaction(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(CustomUser, related_name='transacoes', on_delete=models.CASCADE)
    
    token_origem = models.ForeignKey(Token, related_name='transacoes_origem', on_delete=models.CASCADE)
    quantidade_origem = models.DecimalField(max_digits=30, decimal_places=8)
    
    token_destino = models.ForeignKey(Token, related_name='transacoes_destino', on_delete=models.CASCADE)
    quantidade_destino = models.DecimalField(max_digits=30, decimal_places=8)
    
    def __str__(self):
        return f"{self.usuario.email} - {self.quantidade_origem} {self.token_origem.codigo} => {self.quantidade_destino} {self.token_destino.codigo} em {self.data_hora}"


class Moves(models.Model):
    usuario = models.ForeignKey(CustomUser, related_name='jogadas', on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    ganhou = models.BooleanField()
    quantidade = models.DecimalField(max_digits=30, decimal_places=8)
    
    def __str__(self):
        resultado = "Ganhou" if self.ganhou else "Perdeu"
        return f"{self.usuario.email} - {resultado} {self.quantidade} em {self.data_hora}"

