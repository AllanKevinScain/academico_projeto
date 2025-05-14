from django.shortcuts import render
from . import forms


def contato(request):
    form = forms.ContatoForm()
    dados = {'form': form}

    return render(request, 'contato/contato.html', dados)
