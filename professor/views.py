# -*- encoding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, filters
from .permissions import IsOwnerOrReadOnly, IsOwner
from .models import *
#from .forms import TaskFilter,SprintFilter
from .serializers import *
User = get_user_model()

class DefaultMixin(object):
	"""Configurações default para autenticação, permissões, filtragem e paginação da view"""
	authentication_classes = (
			authentication.BasicAuthentication,
			authentication.TokenAuthentication,
		)
	permission_classes = (
		permissions.IsAuthenticated,
		IsOwner,
		)
	paginate_by = 50
	paginate_by_param = 'page_size'
	max_paginate_by = 100
	filter_backends = (
		filters.DjangoFilterBackend,
		filters.SearchFilter,
		filters.OrderingFilter
		)

class TurmaViewSet(DefaultMixin,viewsets.ModelViewSet):
	queryset = Turma.objects.order_by('nome')
	serializer_class = TurmaSerializer
	search_fields = ('nome','professor')
	ordering_fields = ('nome',)

	def perform_create(self, serializer):
		serializer.save(professor=self.request.user)

	def get_queryset(self):
		self.queryset = super(TurmaViewSet,self).get_queryset()
		self.queryset = self.queryset.filter(professor=self.request.user)
		return self.queryset



class AlunoViewSet(DefaultMixin,viewsets.ModelViewSet):
	queryset = Aluno.objects.order_by('nome')
	serializer_class = AlunoSerializer
	#filter_class = SprintFilter
	search_fields = ('nome','turma')
	ordering_fields = ('nome',)
	
	def get_queryset(self):
		self.queryset = super(AlunoViewSet,self).get_queryset()
		self.queryset = self.queryset.filter(turma__professor=self.request.user)
		return self.queryset

class ComportamentoViewSet(DefaultMixin,viewsets.ModelViewSet):
	queryset = Comportamento.objects.order_by('aluno')
	serializer_class = ComportamentoSerializer
	#filter_class = SprintFilter
	search_fields = ('nome','professor','data',)
	ordering_fields = ('nome','data',)
	
	def get_queryset(self):
		self.queryset = super(ComportamentoViewSet,self).get_queryset()
		self.queryset = self.queryset.filter(aluno__turma__professor=self.request.user)
		return self.queryset

class AulaViewSet(DefaultMixin,viewsets.ModelViewSet):
	queryset = Aula.objects.order_by('data')
	serializer_class = AulaSerializer
	#filter_class = SprintFilter
	search_fields = ('descricao','data','turma')
	ordering_fields = ('data','turma')

	def get_queryset(self):
		self.queryset = super(AulaViewSet,self).get_queryset()
		self.queryset = self.queryset.filter(turma__professor=self.request.user)
		return self.queryset


class AulaAlunoViewSet(DefaultMixin,viewsets.ModelViewSet):
	queryset = AulaAluno.objects.order_by('aluno')
	serializer_class = AulaAlunoSerializer
	#filter_class = SprintFilter
	search_fields = ('aluno','aula',)
	ordering_fields = ('aula',)
	
	def get_queryset(self):
		self.queryset = super(AulaAlunoViewSet,self).get_queryset()
		self.queryset = self.queryset.filter(aula__turma__professor=self.request.user)
		return self.queryset
