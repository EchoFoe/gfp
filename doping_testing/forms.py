from django import forms
from .models import *


class AutopsyForm(forms.ModelForm):
    class Meta:
        model = Autopsy
        exclude = ['created', 'updated']