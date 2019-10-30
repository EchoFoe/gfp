from django.shortcuts import render
from guide.models import *
from .forms import *
from documents.models import *
# from utils.uploadings import UploadingProducts
# from django.contrib import messages


def guide(request):
    all_guides = GuideImage.objects.filter(is_active=True, is_main=True, guide__is_active=True)
    documents = Document.objects.filter(is_active=True)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'guides/guides.html', locals())