from django.shortcuts import render
from broadcast.models import *
from documents.models import *


def broadcast(request):
    broadcasts = Broadcast.objects.filter(is_active=True)
    documents = Document.objects.filter(is_active=True)

    return render(request, 'broadcast/broadcast.html', locals())