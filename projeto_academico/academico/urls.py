from django.urls import path
from .views import index, alunos, cursos
from .views import cadastrar_aluno, cadastrar_curso
from .views import editar_aluno, editar_curso

urlpatterns = [
    path('', index, name='index'),
    path('alunos/', alunos, name='alunos'),
    path('cadastrar_aluno/', cadastrar_aluno, name='cadastrar_aluno'),
    path('editar_aluno/<int:id>/', editar_aluno, name='editar_aluno'),

    path('cursos/', cursos, name='cursos'),
    path('cadastrar_curso/', cadastrar_curso, name='cadastrar_curso'),
    path('editar_curso/<int:id>/', editar_curso, name='editar_curso'),
]
