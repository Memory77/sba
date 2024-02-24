from django import forms 
from .models import PredApi


class PredApiForm(forms.ModelForm):
    class Meta:
        model = PredApi
        fields = "__all__"