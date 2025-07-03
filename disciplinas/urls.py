from django.urls import path
from .views import listar_disciplinas, cadastrar_disciplina, listar_alunos_para_matricula, matricular_aluno, historico_matriculas

app_name = "disciplinas"

urlpatterns = [
    path('', listar_disciplinas, name='lista'),
    path('cadastrar/', cadastrar_disciplina, name='cadastrar'),
    path('listar_alunos__para_matricula/',
         listar_alunos_para_matricula, name='listar_alunos_matricula'),
    path('matricular/<int:aluno_id>/', matricular_aluno, name='matricular'),
    path('historico-matriculas/', historico_matriculas, name='historico'),
]
