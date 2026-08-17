from django.contrib import admin
from ecommerce.models import Produto, Categoria


class Produtos(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "descricao",
        "preco",
        "quantidade_estoque",
        "categoria",
        "criado_em",
    )
    list_display_links = (
        "id",
        "nome",
    )
    list_per_page = 20
    search_fields = ("nome",)


admin.site.register(Produto, Produtos)


class Categorias(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "descricao",
        "criado_em",
    )
    list_display_links = (
        "id",
        "nome",
    )
    search_fields = ("nome",)


admin.site.register(Categoria, Categorias)
