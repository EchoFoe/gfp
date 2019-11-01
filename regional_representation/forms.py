from django import forms
from .models import *


class RegionalForm(forms.ModelForm):
    class Meta:
        model = Regional
        exclude = ['created', 'updated']