from django import forms 
from profiles.models import Profile

class AddProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
    