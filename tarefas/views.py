from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Tarefa
from .serializers import TarefaSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Retorna apenas tarefas do usuário logado
        return Tarefa.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
