from django import forms
from .models import *


class SportsmenForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    dob = forms.DateField(required=True)
    country = forms.CharField(required=True)
    region = forms.CharField(required=True)
    town = forms.CharField(required=True)
    age = forms.ModelChoiceField(queryset=Age_category.objects.filter(is_active=True), required=True)
    weight = forms.ModelChoiceField(queryset=Weight_category.objects.filter(is_active=True), required=True)
    tournament = forms.ModelChoiceField(queryset=Tournament.objects.filter(status_id=1), required=True)
    division = forms.ModelChoiceField(queryset=Division.objects.filter(is_active=True), required=True)
    discipline = forms.ModelChoiceField(queryset=Discipline.objects.filter(is_active=True), required=True)
    team = forms.ModelChoiceField(queryset=Line_up.objects.filter(is_active=True), required=False)
    team_name = forms.CharField(required=False)
    gender = forms.ModelChoiceField(queryset=Gender.objects.filter(is_active=True), required=True)
    trainer = forms.CharField(required=False)

    class Meta:
        model = Sportsman
        exclude = ['created', 'updated']