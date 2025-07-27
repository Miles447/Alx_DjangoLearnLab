from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Document

@permission_required('access_control.can_view', raise_exception=True)
def document_list(request):
    documents = Document.objects.all()
    return render(request, 'access_control/document_list.html', {'documents': documents})

@permission_required('access_control.can_create', raise_exception=True)
def create_document(request):
    return render(request, 'access_control/action_result.html', {'action': 'Create Document'})

@permission_required('access_control.can_edit', raise_exception=True)
def edit_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    return render(request, 'access_control/action_result.html', {'action': f'Edit: {doc.title}'})

@permission_required('access_control.can_delete', raise_exception=True)
def delete_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    return render(request, 'access_control/action_result.html', {'action': f'Delete: {doc.title}'})
