from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from documents.models import *
from tournaments.models import *
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render
from utils.emails import SendingEmail


def sportsman(request):

    documents = Document.objects.filter(is_active=True)
    form = SportsmenForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        print('yes')
        data = form.cleaned_data
        print(form.cleaned_data['email'])
        # new_form = form.save()
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        middle_name = data.get('middle_name')
        email = data.get('email')
        phone = data.get('phone')
        dob = data.get('dob')
        gender = data.get('gender')
        weight = data.get('weight')
        age = data.get('age')
        country = data.get('country')
        region = data.get('region')
        town = data.get('town')
        team = data.get('team')
        trainer = data.get('trainer')
        tournament = data.get('tournament')
        division = data.get('division')
        discipline = data.get('discipline')

        # user, created = User.objects.get_or_create(username=phone, defaults={"first_name": first_name, "email": email})
        order = Sportsman.objects.create(first_name=first_name, last_name=last_name, middle_name=middle_name, email=email, phone=phone, dob=dob, gender_id=gender, weight_id=weight, age_id=age, country=country, region=region, town=town, team_id=team, trainer=trainer, tournament_id=tournament, division_id=division, discipline_id=discipline)
        # order = Sportsman.objects.update()

        email = SendingEmail()
        email.sending_email(type_id=1, order=order)
        email.sending_email(type_id=2, email=order.email, order=order)
        return HttpResponseRedirect('/thanks/')
    else:
        form = SportsmenForm()
    return render(request, 'sportsman/sportsman.html', locals())


# def sportsman(request):
#     documents = Document.objects.filter(is_active=True)
#     form = SportsmenForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         print(request.POST)
#         print(form.cleaned_data)
#         print("yes")
#         data = form.cleaned_data
#         print(form.cleaned_data["email"])
#         new_form = form.save()
#         data = request.POST
#         first_name = data.get('first_name', "3423453")
#         phone = data['phone']
#         email = data.get('email')
#
#         # user, created = User.objects.get_or_create(username=phone, defaults={"first_name": first_name, "email": email})
#
#         order = Sportsman.objects.create(first_name=first_name, phone=phone,
#                                          email=email)
#
#         email = SendingEmail()
#         email.sending_email(type_id=1, order=order)
#         email.sending_email(type_id=2, email=order.email, order=order)
#         return HttpResponseRedirect(request.META['HTTP_REFERER'])
#     else:
#         form = SportsmenForm()
#     return render(request, 'sportsman/sportsman.html', locals())
