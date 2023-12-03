from django.urls import path
from apps.cafeteria.views import *

urlpatterns = [
    path('', index, name = "index"),
    path('produto/<int:produto_id>', produto, name = "produto"),
    path('buscar', buscar, name="buscar"),
    path('cadastrar_produto', cadastrar_produto, name="cadastrar_produto"),
    path('editar_produto/<int:produto_id>', editar_produto, name="editar_produto"),
    path('deletar_produto/<int:produto_id>', deletar_produto, name="deletar_produto"),
    path('filtro/<str:categoria>', filtro, name='filtro'),
]
