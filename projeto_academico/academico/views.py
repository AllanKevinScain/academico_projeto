from django.shortcuts import render
from .models import Aluno, Curso
from .forms import CursoForm, AlunoForm
from django.shortcuts import redirect


def index(request):
    return render(request, 'academico/index.html')


def alunos(request):
    alunos = Aluno.objects.all()
    dados = {'alunos': alunos}
    return render(request, 'academico/aluno/lista_alunos.html', dados)


# Nem ta sendo usado ainda
def cursos(request):
    cursos = Curso.objects.all()
    dados = {'cursos': cursos}
    return render(request, 'academico/aluno/lista_alunos.html', dados)


def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunos')
    else:
        form = AlunoForm()
        dados = {'form': form}
    return render(request, 'academico/aluno/cadastrar_aluno.html', dados)


def cadastrar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            # is_valid() Vai validar os dados, o Tokken CSRF, e criar um
            # dicionário com os dados chamado cleaned_data
            # Aqui estamos pegando o nome do curso
            curso = form.cleaned_data['nome']
            print(curso)

            form.save()
            return redirect('index')
    else:
        form = CursoForm()
        dados = {'form': form}
    return render(request, 'academico/aluno/cadastrar_curso.html', dados)


def editar_aluno(request, id):
    try:
        aluno = Aluno.objects.get(id=id)
    except:
        return redirect('alunos')

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('alunos')

    form = AlunoForm(instance=aluno)
    dados = {'form': form, 'aluno': aluno}

    return render(request, 'academico/aluno/editar_aluno.html', dados)
