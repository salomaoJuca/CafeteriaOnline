from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from djmoney.models.fields import MoneyField

# Create your models here.
class Produto(models.Model):

    OPCOES_CATEGORIA = [
        ("QUENTE", "Cafés quentes")
        ,("GELADO", "Cafés Gelados")
        ,("CHA", "Chás")
        ,("PADARIA", "Padaria")
        ,("REFEICAO", "Refeições")
    ]
    denominacao = models.CharField(max_length=100, null= False, blank=False)
    legenda = models.CharField(max_length=100, null= False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default="")
    descricao = models.TextField(null=False, blank=False)
    valor = MoneyField(max_digits=8, decimal_places=2, default_currency='BRL', null = False, default= 0)
    imagem = models.ImageField(upload_to="imagens/produto/", blank=True)
    publicada = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User
        ,on_delete=models.SET_NULL
        ,null=True
        ,blank=False
        ,related_name="user"
    )

    def __str__(self):
        return self.denominacao
