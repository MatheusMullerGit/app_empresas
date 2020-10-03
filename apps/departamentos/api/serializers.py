from rest_framework import serializers
from apps.departamentos.models import Departamento
from apps.funcionarios.api.serializers import FuncionarioSerializer

class DepartamentoSerializer(serializers.ModelSerializer):
    funcionario_set = FuncionarioSerializer(many=True)
    class Meta:
        model = Departamento
        fields = ['nome', 'empresa', 'funcionario_set']
