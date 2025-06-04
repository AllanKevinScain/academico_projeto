from django.urls import path
from .views import index, alunos, cursos
from .views import cadastrar_aluno, cadastrar_curso, excluir_aluno, alunos_inativos, ativar_aluno, ordenar_alunos, ordenar_alunos_inativos
from .views import editar_aluno, editar_curso, excluir_curso

urlpatterns = [
    path('', index, name='index'),
    path('alunos/', alunos, name='alunos'),
    path('alunos/inativos/', alunos_inativos, name='alunos_inativos'),
    path('cadastrar_aluno/', cadastrar_aluno, name='cadastrar_aluno'),
    path('editar_aluno/<int:id>/', editar_aluno, name='editar_aluno'),
    path('excluir_aluno/<int:id>/', excluir_aluno, name='excluir_aluno'),
    path('alunos/ativar/<int:id>/', ativar_aluno, name='ativar_aluno'),
    path('alunos/ordenar/<parametro>/', ordenar_alunos, name='ordenar_alunos'),
    path('alunos/ordenar/inativos/<parametro>/',
         ordenar_alunos_inativos, name='ordenar_alunos_inativos'),

    path('cursos/', cursos, name='cursos'),
    path('cadastrar_curso/', cadastrar_curso, name='cadastrar_curso'),
    path('editar_curso/<int:id>/', editar_curso, name='editar_curso'),
    path('excluir_curso/<int:id>/', excluir_curso, name='excluir_curso'),
]
