from django.contrib import admin
from .models import *

# i) Ocupação e pessoas
class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]

# ii) Instituição e cursos
class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

# iii) Área do saber e cursos
class CursoAreaInline(admin.TabularInline):
    model = Curso
    extra = 1

class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoAreaInline]

# iv) Cursos e disciplinas (relacionamento está em CursoDisciplina)
class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline]

# v) Disciplinas e avaliações
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

# vi) Turmas e alunos — não está claro onde está a relação, então ignorando por enquanto

# vii) UF e cidades — não há um modelo UF, mas agrupando cidades pelo campo `uf`

class CidadeAdmin(admin.ModelAdmin):
    list_filter = ['uf']
    search_fields = ['nome']

# ix) Estudantes, disciplinas, avaliações, frequência — múltiplas ligações
class AvaliacaoPessoaInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class PessoaAdmin(admin.ModelAdmin):
    inlines = [FrequenciaInline]
    search_fields = ['nome', 'cpf']

# Registrar tudo
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(InstituicaoEnsino, InstituicaoEnsinoAdmin)
admin.site.register(AreaSaber, AreaSaberAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turma)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(AvaliacaoTipo)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turno)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
