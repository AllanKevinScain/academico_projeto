from django.shortcuts import render
from . import forms
from django.core.mail import send_mail


def contato(request):
    if request.method == 'POST':
        form = forms.ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            corpo_email = f"Mensagem de: {nome}\n\n Email: {email}\n\n Mensagem: {mensagem}"

            send_mail(
                assunto,
                corpo_email,
                email,
                ['meuemail44allan@gmail.com'],
            )

            form = forms.ContatoForm()
            dados = {
                'form': form,
                'mensagem_enviada': True,
                'mensagem': 'Mensagem enviada com sucesso!',
            }

    else:
        form = forms.ContatoForm()
        dados = {'form': form}

    return render(request, 'contato/contato.html', dados)
