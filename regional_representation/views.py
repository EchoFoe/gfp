from django.shortcuts import render
from .forms import *
from documents.models import *
from regional_representation.models import *


def regional_representation(request):
    documents = Document.objects.filter(is_active=True)

    form = RegionalForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data['email'])
        new_form = form.save()

    return render(request, 'regional_representation/regional_representation.html', locals())