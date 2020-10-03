from rest_framework import viewsets
from apps.empresas.api.serializers import EmpresaSerializer
from apps.empresas.models import Empresa


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    