import hashlib

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from main.forms import DocumentForm
from main.models import Document


class DocumentCreateView(LoginRequiredMixin, CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'main/upload.html'
    success_url = reverse_lazy('main:index')
    login_url = 'login'

    def form_valid(self, form):
        hc = hashlib.sha256(
            form.cleaned_data['document'].name.encode()
        ).hexdigest()
        # self.render_to_response(self.get_context_data(form=form))
        if Document.objects.filter(hash_code=hc).exists():
            form.add_error(
                'document',
                (
                    'Файл с таким именем '
                    f'{form.cleaned_data["document"].name} существует.'
                ),
            )
            return self.render_to_response(self.get_context_data(form=form))

        instance = form.save(commit=False)
        instance.content_type = form.cleaned_data['document'].content_type
        instance.hash_code = hc
        instance.owner = self.request.user
        instance.save()

        return redirect('main:index')


class DocumentListView(ListView):
    model = Document
    template_name = 'main/documents.html'
    context_object_name = 'documents'


def download(request, doc_id):
    doc = get_object_or_404(Document, pk=doc_id)
    response = HttpResponse(doc.document, content_type=doc.content_type)
    file_name = doc.document.name.split('/')[-1]
    response['Content-Disposition'] = f'attachment;' f'filename="{file_name}"'
    return response
