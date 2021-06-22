from django import forms
from src.backend.models import Profile

class ProfileList(forms.ModelForm):
    innset = forms.CharField()
    class Meta:
        model = Profile
        fields = ('user','check','innset')
