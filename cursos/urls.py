from django.urls import path
from .views import cursos, cadastrar_curso, editar_curso, excluir_curso

app_name = "cursos"

urlpatterns = [
    path('', cursos, name='lista'),
    path('cadastrar/', cadastrar_curso, name='cadastrar'),
    path('editar/<int:id>/', editar_curso, name='editar'),
    path('excluir/<int:id>/', excluir_curso, name='excluir'),
]
