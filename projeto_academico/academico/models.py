from django.db import models

GENERO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
]

ESTADO_CIVIL_CHOICES = [
    ('S', 'Solteiro'),
    ('C', 'Casado'),
    ('D', 'Divorciado'),
    ('V', 'Viúvo'),
]

ESCOLARIDADE_CHOICES = [
    ('fun', 'Fundamental'),
    ('med', 'Médio'),
    ('sup', 'Superior'),
    ('pos', 'Pós-graduação'),
    ('mes', 'Mestrado'),
    ('dou', 'Doutorado'),
]


class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    genero = models.CharField(max_length=2, choices=GENERO_CHOICES)
    estado_civil = models.CharField(
        max_length=30, choices=ESTADO_CIVIL_CHOICES)
    escolaridade = models.CharField(
        max_length=50, choices=ESCOLARIDADE_CHOICES)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
