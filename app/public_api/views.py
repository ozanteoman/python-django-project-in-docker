from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Document, PrivateDocument


# Create your views here.

def index(request):
    return render(request, 'index.html', context={})


class DocumentCreateView(CreateView):
    model = Document
    fields = ['upload', ]
    success_url = reverse_lazy('home')
    template_name = 'document_form_html.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Document.objects.all()
        context['documents'] = documents
        return context


class PrivateDocumentCreateView(CreateView):
    model = PrivateDocument
    fields = ['upload', ]
    success_url = reverse_lazy('home')
    template_name = 'document_form_html.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = PrivateDocument.objects.all()
        context['documents'] = documents
        return context
