from django.urls import path
from .views import index, alunos
from .views import cadastrar_aluno, cadastrar_curso
from .views import editar_aluno

urlpatterns = [
    path('', index, name='index'),
    path('alunos/', alunos, name='alunos'),
    path('cadastrar_aluno/', cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastrar_curso/', cadastrar_curso, name='cadastrar_curso'),
    path('editar_aluno/<int:id>/', editar_aluno, name='editar_aluno'),
]
