from django.db import models
from django.contrib.auth.models import User
from apps.empresas.models import Empresa

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    empresas = models.ManyToManyField(Empresa)
    
    def __str__(self):
        return self.nome
