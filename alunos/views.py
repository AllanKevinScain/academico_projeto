from django.shortcuts import render
from .models import Aluno
from .forms import AlunoForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

ORDENACAO_ALUNOS_LOOKUP = {
    'curso': 'curso__nome',
    'nome': 'nome',
    'genero': 'genero',
    'escolaridade': 'escolaridade',
    'estado_civil': 'estado_civil',
    'data_nascimento': 'data_nascimento'
}


@login_required
def alunos(request):
    query = request.GET.get('busca', '')
    if query:
        alunos = Aluno.objects.filter(ativo=True, nome__icontains=query)
    else:
        alunos = Aluno.objects.filter(ativo=True)
    dados = {'alunos': alunos, 'ativos': True, 'query': query}
    return render(request, 'alunos/lista.html', dados)


@login_required
def alunos_inativos(request):
    alunos = Aluno.objects.filter(ativo=False)
    dados = {'alunos': alunos, 'ativos': False}
    return render(request, 'alunos/lista.html', dados)


@login_required
def cadastrar_aluno(request):

    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('alunos:lista')
    else:
        form = AlunoForm()
        dados = {
            'form': form,
        }
    return render(request, 'alunos/cadastrar.html', dados)


@login_required
def editar_aluno(request, id):

    try:
        aluno = Aluno.objects.get(id=id)
    except:
        return redirect('alunos:lista')

    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('alunos:lista')

    # form vai receber um formulário com os dados do aluno selecionado.
    form = AlunoForm(instance=aluno)

    # Montamos o dicionário com os dados para ser passado para o template.
    dados = {
        'form': form,
        'aluno': aluno,
    }

    return render(request, 'alunos/editar.html', dados)


@login_required
def excluir_aluno(request, id):
    try:
        aluno = Aluno.objects.get(id=id)
        aluno.ativo = False
        aluno.save()
        messages.success(request, "Aluno excluído com sucesso.")
    except Aluno.DoesNotExist:
        messages.error(request, "Aluno não encontrado.")

    return redirect('alunos:lista')


@login_required
def ativar_aluno(request, id):
    try:
        aluno = Aluno.objects.get(id=id)
    except Aluno.DoesNotExist:
        messages.error(request, "Aluno não encontrado.")
        return redirect('alunos:lista_inativos')

    if aluno.ativo == False:
        aluno.ativo = True
        aluno.save()
        messages.success(request, "Aluno reativado com sucesso.")

    else:
        messages.info(request, "O aluno já está ativo.")

    return redirect('alunos:lista_inativos')


@login_required
def ordenar_alunos(request, parametro):
    campo_ordenacao = ORDENACAO_ALUNOS_LOOKUP.get(parametro)
    busca = request.GET.get('busca', '')
    alunos = Aluno.objects.filter(ativo=True)

    if busca:
        alunos = alunos.filter(nome__icontains=busca)

    alunos = alunos.order_by(campo_ordenacao)
    dados = {'alunos': alunos, 'ativos': True, 'query': busca}
    return render(request, 'alunos/lista.html', dados)


@login_required
def ordenar_alunos_inativos(request, paramtero):
    campo_ordenacao = ORDENACAO_ALUNOS_LOOKUP.get(paramtero)
    busca = request.GET.get('busca', '')
    alunos = Aluno.objects.filter(ativo=False)

    if busca:
        alunos = Aluno.objects.filter(nome__icontains=busca)

    alunos = alunos.order_by(campo_ordenacao)
    dados = {'alunos': alunos, 'ativos': False, 'query': busca}
    return render(request, 'alunos/lista.html', dados)


@login_required
def detalhes_aluno(request, aluno_id):
    try:
        aluno = Aluno.objects.get(id=aluno_id)
    except Aluno.DoesNotExist:
        messages.error(request, "Aluno não encontrado.")
        return redirect('alunos:lista')

    dados = {
        'aluno': aluno,
    }

    return render(request, 'alunos/detalhes.html', dados)
