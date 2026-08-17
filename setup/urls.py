from django.contrib import admin
from django.urls import path, include
from ecommerce.views import ProdutoViewSet, CategoriaViewSet
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Documentação da API",
        default_version="v1",
        description="Documentação da API de um E-commerce",
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register("produtos", ProdutoViewSet, basename="Produtos")
router.register("categorias", CategoriaViewSet, basename="Categorias")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
