from rest_framework import serializers
from apps.empresas.models import Empresa
from apps.funcionarios.api.serializers import FuncionarioSerializer

class EmpresaSerializer(serializers.ModelSerializer):
    funcionario_set = FuncionarioSerializer(many=True)
    class Meta:
        model = Empresa
        fields = ['id', 'nome', 'funcionario_set']
