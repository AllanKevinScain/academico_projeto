from django.urls import path
from .views import alunos, alunos_inativos, ordenar_alunos, ordenar_alunos_inativos
from .views import cadastrar_aluno, excluir_aluno, ativar_aluno, detalhes_aluno
from .views import editar_aluno

app_name = "alunos"

urlpatterns = [
    path('', alunos, name='lista'),
    path('inativos/', alunos_inativos, name='lista_inativos'),
    path('cadastrar/', cadastrar_aluno, name='cadastrar'),
    path('editar/<int:id>/', editar_aluno, name='editar'),
    path('excluir/<int:id>/', excluir_aluno, name='excluir'),
    path('ativar/<int:id>/', ativar_aluno, name='ativar'),
    path('ordenar/<parametro>/', ordenar_alunos, name='ordenar'),
    path('ordenar/inativos/<parametro>/',
         ordenar_alunos_inativos, name='ordenar_inativos'),
    path('aluno/<int:aluno_id>/', detalhes_aluno, name='detalhes'),
]
