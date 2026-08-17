from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=500, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.CharField(max_length=1000, null=True, blank=True)
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    quantidade_estoque = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Informe a quantidade em estoque.",
        null=False,
        blank=False,
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, null=False, blank=False
    )
    imagem = models.URLField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
