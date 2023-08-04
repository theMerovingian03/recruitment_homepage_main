from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'

# Reording Form and View

class PositionForm(forms.Form):
    position = forms.CharField()