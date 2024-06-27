from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/<int:id>/', views.cliente_detail, name='cliente_detail'),
    path('clientes/novo/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:id>/editar/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:id>/deletar/', views.cliente_delete, name='cliente_delete'),
    path('clientes/<int:id>/exames/', views.exame_list, name='exame_list'),
    path('clientes/<int:id>/exames/novo/', views.exame_create, name='exame_create'),
    path('clientes/<int:cliente_id>/exames/<int:id>/editar/', views.exame_update, name='exame_update'),
    path('clientes/<int:cliente_id>/exames/<int:id>/deletar/', views.exame_delete, name='exame_delete'),
    path('exames/<int:id>/', views.exame_detail, name='exame_detail'),
    path('exames/', views.exame_list_all, name='exame_list_all'),
]