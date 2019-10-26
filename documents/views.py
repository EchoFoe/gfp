from django.shortcuts import render
from documents.models import *


def document(request):
    documents = Document.objects.filter(is_active=True)

    return render(request, 'navbar/navbar.html', locals())