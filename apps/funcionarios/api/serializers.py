from rest_framework import serializers
from apps.funcionarios.models import Funcionario

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'departamentos', 'empresa', 'user']
