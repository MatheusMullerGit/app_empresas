from django.views.generic.edit import CreateView, UpdateView
from .models import Documento
from django.urls import reverse

class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('update_funcionario', args=[self.kwargs['funcionario_id']])
