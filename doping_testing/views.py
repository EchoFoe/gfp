from django.shortcuts import render
from .forms import *
from documents.models import *
from doping_testing.models import *


def doping_testing(request):
    documents = Document.objects.filter(is_active=True)
    drugs = Doping.objects.filter(is_active=True)
    all_list = Autopsy.objects.filter(is_active=True)
    positive_list = all_list.filter(status_id=2)
    not_positive_list = all_list.filter(status_id=3)

    form = AutopsyForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data['email'])
        new_form = form.save()

    return render(request, 'doping_testing/doping_testing.html', locals())


def disqualified_list(request):
    documents = Document.objects.filter(is_active=True)
    drugs = Doping.objects.filter(is_active=True)
    all_list = Autopsy.objects.filter(is_active=True)
    positive_list = all_list.filter(status_id=2)
    not_positive_list = all_list.filter(status_id=3)

    form = AutopsyForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data['email'])
        new_form = form.save()

    return render(request, 'doping_testing/disqualified_list.html', locals())