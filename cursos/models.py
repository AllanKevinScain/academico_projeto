from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.formatar_nome_curso(self.nome)
        super().save(*args, **kwargs)

    def formatar_nome_curso(self, nome):
        partes = nome.lower().split()
        minusculas = ['da', 'de', 'do', 'das', 'dos', 'e',
                      'em', 'a', 'o', 'as', 'os', 'para', 'com']

        return ' '.join([
            p if p in minusculas else p.capitalize()
            for p in partes
        ])
