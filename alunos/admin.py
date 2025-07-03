from django.contrib import admin
from .models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'curso')
    search_fields = ('nome',)
    list_filter = ('curso',)
