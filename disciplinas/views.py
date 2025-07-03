from django.shortcuts import render, redirect
from .forms import DisciplinaForm
from django.contrib import messages
from .models import Disciplina, Aluno, Matricula
from django.contrib.auth.decorators import login_required


@login_required
def cadastrar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Disciplina cadastrada com sucesso!')
            return redirect('disciplinas:cadastrar')
    else:
        form = DisciplinaForm()
        dados = {
            'form': form
        }
    return render(request, 'disciplinas/cadastrar.html', dados)


@login_required
def listar_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    dados = {
        'disciplinas': disciplinas
    }
    return render(request, 'disciplinas/lista.html', dados)


@login_required
def listar_alunos_para_matricula(request):
    busca = request.GET.get('busca', '')
    if busca:
        alunos = Aluno.objects.filter(nome__icontains=busca, ativo=True)
    else:
        alunos = Aluno.objects.filter(ativo=True)

    dados = {
        'alunos': alunos,
        'busca': busca
    }
    return render(request, 'disciplinas/lista_alunos_matricula.html', dados)


@login_required
def matricular_aluno(request, aluno_id):
    try:
        aluno = Aluno.objects.get(id=aluno_id)
    except Aluno.DoesNotExist:
        return redirect('disciplinas:listar_alunos_matricula')

    # Só disciplinas do curso do aluno
    disciplinas_disponiveis = Disciplina.objects.filter(curso=aluno.curso)

    if request.method == 'POST':
        # Aqui vamos pegar os IDs das disciplinas selecionadas lá no formulário:
        disciplinas_selecionadas_id = request.POST.getlist('disciplinas')

        # Vamos testar se o foi marcado pelo menos uma disciplina:
        if not disciplinas_selecionadas_id:
            messages.error(
                request, 'Você deve selecionar pelo menos uma disciplina.')
            dados = {
                'aluno': aluno,
                'disciplinas': disciplinas_disponiveis
            }
            return render(request, 'disciplinas/matriculas.html', dados)

        # Aqui vamos criar uma nova matrícula para o aluno:
        matricula = Matricula.objects.create(aluno=aluno)

        # Associa as disciplinas selecionadas à matrícula criada:
        matricula.disciplinas.set(disciplinas_selecionadas_id)

        messages.success(request, 'Matrícula realizada com sucesso!')
        return redirect('disciplinas:listar_alunos_matricula')

    dados = {
        'aluno': aluno,
        'disciplinas': disciplinas_disponiveis
    }
    return render(request, 'disciplinas/matriculas.html', dados)


@login_required
def historico_matriculas(request):
    matriculas = Matricula.objects.all().order_by('-id')
    dados = {
        'matriculas': matriculas
    }
    return render(request, 'disciplinas/historico.html', dados)
