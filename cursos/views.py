from django.shortcuts import render
from .models import Curso
from .forms import CursoForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def cursos(request):
    cursos = Curso.objects.all()
    dados = {'cursos': cursos}
    return render(request, 'cursos/lista.html', dados)


@login_required
def cadastrar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos:lista')
    else:
        form = CursoForm()
        dados = {'form': form}
    return render(request, 'cursos/cadastrar.html', dados)


@login_required
def editar_curso(request, id):
    try:
        curso = Curso.objects.get(id=id)
    except:
        return redirect('cursos:lista')

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos:lista')

    form = CursoForm(instance=curso)
    dados = {'form': form, 'curso': curso}

    return render(request, 'cursos/editar.html', dados)


@login_required
def excluir_curso(request, id):
    try:
        curso = Curso.objects.get(id=id)
        curso.delete()
        messages.success(request, "Curso excluído com sucesso.")
    except RestrictedError:
        messages.error(
            request, "Não é possível deletar o curso pois há alunos vinculados.")
    except Curso.DoesNotExist:
        messages.error(request, "Curso não encontrado.")

    return redirect('cursos:lista')
