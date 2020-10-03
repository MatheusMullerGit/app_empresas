from rest_framework import viewsets
from apps.departamentos.api.serializers import DepartamentoSerializer
from apps.departamentos.models import Departamento


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer