from ecommerce.models import Produto, Categoria
from ecommerce.serializers import CategoriaSerializer, ProdutoSerializer
from rest_framework import viewsets


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by("id")
    serializer_class = ProdutoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by("id")
    serializer_class = CategoriaSerializer
