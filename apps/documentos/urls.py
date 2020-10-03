from django.urls import path
from .views import DocumentoCreate#, DocumentEdit

urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentoCreate.as_view(), name='create_documento'),
#    path('editar/<int:pk>/',
#         DocumentEdit.as_view(), name='edit_document'),
]
