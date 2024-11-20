#Here the paths that localhost will follow when manage.py is initialized were created
#Here also occurs the path that each page follows with communication between them
from django.urls import path
from . import views
from .views import adicionar_funcionario, listar_funcionario, excluir_funcionario
urlpatterns = [
    path('adicionar/', views.adicionar_funcionario, name='adicionar_funcionario'),
    path('listar/', views.listar_funcionario, name='listar_funcionario'),
    path('', views.index, name='index'),
    path('excluir/<str:codigo>/', excluir_funcionario, name='excluir_funcionario'),
    path('funcionario/editar/<int:pk>/', views.editar_funcionario, name='editar_funcionario'),

]