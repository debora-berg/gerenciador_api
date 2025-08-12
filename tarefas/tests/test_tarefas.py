import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from tarefas.models import Tarefa

pytestmark = pytest.mark.django_db  

@pytest.fixture
def client_autenticado():
    usuario = User.objects.create_user(username="teste", password="123")
    client = APIClient()
    client.force_authenticate(user=usuario)
    return client, usuario

def test_criar_tarefa(client_autenticado):
    client, usuario = client_autenticado
    dados = {"titulo": "Tarefa 1", "descricao": "Descrição da tarefa"}
    response = client.post("/api/tarefas/", dados, format="json")
    assert response.status_code == 201
    assert response.data["titulo"] == "Tarefa 1"

def test_listar_tarefas(client_autenticado):
    client, usuario = client_autenticado
    Tarefa.objects.create(titulo="Tarefa Existente", descricao="Descrição", usuario=usuario)
    response = client.get("/api/tarefas/")
    assert response.status_code == 200
    assert len(response.data) >= 1

def test_atualizar_tarefa(client_autenticado):
    client, usuario = client_autenticado
    tarefa = Tarefa.objects.create(titulo="Tarefa Antiga", descricao="Descrição", usuario=usuario)
    dados = {"titulo": "Tarefa Atualizada", "descricao": "Descrição atualizada"}
    url = f"/api/tarefas/{tarefa.id}/"
    response = client.put(url, dados, format="json")
    assert response.status_code == 200
    assert response.data["titulo"] == "Tarefa Atualizada"

def test_deletar_tarefa(client_autenticado):
    client, usuario = client_autenticado
    tarefa = Tarefa.objects.create(titulo="Tarefa para deletar", descricao="Descrição", usuario=usuario)
    url = f"/api/tarefas/{tarefa.id}/"
    response = client.delete(url)
    assert response.status_code == 204
