from django.urls import path
from .views import index, alunos, cadastrar_aluno, cadastrar_curso

urlpatterns = [
    path('', index, name='index'),
    path('alunos/', alunos, name='alunos'),
    path('cadastrar_aluno/', cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastrar_curso/', cadastrar_curso, name='cadastrar_curso'),
]
