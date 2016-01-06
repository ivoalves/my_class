# -*- encoding: utf-8 -*-
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r'turmas',views.TurmaViewSet)
router.register(r'alunos',views.AlunoViewSet)
router.register(r'comportamentos',views.ComportamentoViewSet)
router.register(r'aula',views.AulaViewSet)
router.register(r'aula_aluno',views.AulaAlunoViewSet)
