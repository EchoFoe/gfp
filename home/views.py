from django.shortcuts import render
from .forms import *
# from sportsman.models import *
from tournaments.models import *
from reviews.models import *
from documents.models import *


def home(request):
    all_tournaments = TournamentImage.objects.filter(is_active=True, is_main=True, tournament__is_active=True)
    new_tournaments = all_tournaments.filter(tournament__status_id=1).order_by('tournament__start_time')
    held_tournaments = all_tournaments.filter(tournament__status_id=2)
    canceled_tournaments = all_tournaments.filter(tournament__status_id=3)
    failed_tournaments = all_tournaments.filter(tournament__status_id=4)
    all_reviews = ReviewImage.objects.filter(is_active=True, is_main=True, review__is_active=True)
    documents = Document.objects.filter(is_active=True)

    return render(request, 'home/home.html', locals())


def photo_and_video(request):
    all_tournaments = TournamentImage.objects.filter(is_active=True, is_main=True, tournament__is_active=True)
    held_tournaments = all_tournaments.filter(tournament__status_id=2)
    documents = Document.objects.filter(is_active=True)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data['email'])
        new_form = form.save()

    return render(request, 'photo_and_video/photo_and_video.html', locals())


def thanks(request):
    documents = Document.objects.filter(is_active=True)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data['email'])
        new_form = form.save()

    return render(request, 'thanks/thanks.html', locals())
