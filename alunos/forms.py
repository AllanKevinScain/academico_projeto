from django import forms
from .models import Aluno


class AlunoForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Aluno
        fields = ['foto', 'nome', 'data_nascimento', 'cpf', 'genero',
                  'estado_civil', 'escolaridade', 'curso']
