from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    concluida = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
