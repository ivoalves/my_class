# -*- encoding: utf-8 -*-
from datetime import date
from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from .models import *
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	#links = serializers.SerializerMethodField()
	full_name = serializers.CharField(source='get_full_name',read_only=True)
	
	class Meta:
		model = User
		fields = ('id',User.USERNAME_FIELD,'full_name','is_active',)

	def get_links(self,obj):
		request = self.context['request']
		username = obj.get_username()
		return {
			'self':reverse('user-detail',kwargs={User.USERNAME_FIELD:username},request=request),
		}

class TurmaSerializer(serializers.ModelSerializer):
	#links = serializers.SerializerMethodField()
	professor = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD,read_only=True,required=False)
	
	class Meta:
		model = Turma
		fields = ('id','nome','professor',)

	def get_links(self,obj):
		request = self.context['request']
		return {
			'self':reverse('turma-detail',kwargs={'pk':obj.pk},request=request),
			'alunos':reverse('aluno-list',request=request) + "?sprint={}".format(obj.pk),
		}

class AlunoSerializer(serializers.ModelSerializer):
	#links = serializers.SerializerMethodField()
	
	class Meta:
		model = Aluno
		fields = ('id','nome','turma',)

	def get_links(self,obj):
		request = self.context['request']
		return {
			'self':reverse('sprint-detail',kwargs={'pk':obj.pk},request=request),
			'tasks':reverse('task-list',request=request) + "?sprint={}".format(obj.pk),
		}

class ComportamentoSerializer(serializers.ModelSerializer):
	#links = serializers.SerializerMethodField()
	
	class Meta:
		model = Comportamento
		fields = ('id','comentario','aluno','positivo','data')

	def get_links(self,obj):
		request = self.context['request']
		return {
			'self':reverse('sprint-detail',kwargs={'pk':obj.pk},request=request),
			'tasks':reverse('task-list',request=request) + "?sprint={}".format(obj.pk),
		}

class AulaSerializer(serializers.ModelSerializer):
	#links = serializers.SerializerMethodField()
	
	class Meta:
		model = Aula
		fields = ('id','descricao','data','turma')

	def get_links(self,obj):
		request = self.context['request']
		return {
			'self':reverse('sprint-detail',kwargs={'pk':obj.pk},request=request),
			'tasks':reverse('task-list',request=request) + "?sprint={}".format(obj.pk),
		}

class AulaAlunoSerializer(serializers.ModelSerializer):
	#links = serializers.SerializerMethodField()
	
	class Meta:
		model = AulaAluno
		fields = ('id','aula','aluno','presente')

	def get_links(self,obj):
		request = self.context['request']
		return {
			'self':reverse('sprint-detail',kwargs={'pk':obj.pk},request=request),
			'tasks':reverse('task-list',request=request) + "?sprint={}".format(obj.pk),
		}