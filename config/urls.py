from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),

    path('pessoa/', PessoaView.as_view(), name='pessoa'),                  # RF01
    path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),             # RF02
    path('instituicao/', InstituicaoEnsinoView.as_view(), name='instituicao'),  # RF03
    path('area-saber/', AreaSaberView.as_view(), name='area_saber'),        # RF04
    path('curso/', CursoView.as_view(), name='curso'),                      # RF05
    path('turma/', TurmaView.as_view(), name='turma'),                      # RF06
    path('disciplina/', DisciplinaView.as_view(), name='disciplina'),       # RF07
    path('matricula/', MatriculaView.as_view(), name='matricula'),          # RF08
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),          # RF09
    path('frequencia/', FrequenciaView.as_view(), name='frequencia'),       # RF10
    path('turno/', TurnoView.as_view(), name='turno'),                      # RF11
    path('cidade/', CidadeView.as_view(), name='cidade'),                   # RF12
    path('ocorrencia/', OcorrenciaView.as_view(), name='ocorrencia'),       # RF13
    path('curso-disciplina/', CursoDisciplinaView.as_view(), name='curso_disciplina'),  # RF14
    path('tipo-avaliacao/', AvaliacaoTipoView.as_view(), name='tipo_avaliacao'),         # RF15
]
