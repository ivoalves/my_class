from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

class Turma(models.Model):
	nome =  models.CharField(max_length=255)
	professor = models.ForeignKey(User)

class Aluno(models.Model):
	nome = models.CharField(max_length=255)
	imagem =  models.ImageField(upload_to='alunos',null=True,blank=True)
	turma = models.ForeignKey(Turma)

class Comportamento(models.Model):
	comentario = models.CharField(max_length=255)
	aluno = models.ForeignKey(Aluno)
	#turma = models.Turma(Turma)
	positivo = models.BooleanField(default=True)
	data = models.DateField(default=timezone.now,null=True,blank=True)

class Aula(models.Model):
	descricao = models.TextField()
	data = models.DateField(null=True,blank=True)
	turma = models.ForeignKey(Turma)

class AulaAluno(models.Model):
	presente = models.BooleanField(default=True)
	aluno = models.ForeignKey(Aluno)
	aula = models.ForeignKey(Aula)	
