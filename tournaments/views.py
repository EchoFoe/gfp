from django.shortcuts import render
from tournaments.models import *
from .forms import *
from documents.models import *
# from utils.uploadings import UploadingProducts
# from django.contrib import messages


def tournament(request, tournament_id):
    tournaments = Tournament.objects.get(id=tournament_id)
    # tournaments = Tournament.objects.filter(status_id=1)
    all_tournaments = TournamentImage.objects.filter(is_active=True, is_main=True, tournament__is_active=True)
    new_tournaments = all_tournaments.filter(tournament__status_id=1)
    documents = Document.objects.filter(is_active=True)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'tournaments/tournament.html', locals())