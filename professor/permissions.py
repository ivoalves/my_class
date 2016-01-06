# -*- encoding: utf-8 -*-
from rest_framework import permissions
from .models import *

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        if isinstance(obj, Turma ):
            return obj.professor == request.user
        if isinstance(obj, Aluno ):
            return obj.turma.professor == request.user
        if isinstance(obj, Comportamento ):
            return obj.aluno.turma.professor == request.user
        if isinstance(obj, Aula ):
            return obj.turma == request.user
        if isinstance(obj, AulaAluno ):
            return obj.aula.turma.professor == request.user
        # Write permissions are only allowed to the owner of the snippet.
        return True

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        
        if isinstance(obj, Turma ):
            return obj.professor == request.user
        if isinstance(obj, Aluno ):
            return obj.turma.professor == request.user
        if isinstance(obj, Comportamento ):
            return obj.aluno.turma.professor == request.user
        if isinstance(obj, Aula ):
            return obj.turma == request.user
        if isinstance(obj, AulaAluno ):
            return obj.aula.turma.professor == request.user
        # Write permissions are only allowed to the owner of the snippet.
        return True