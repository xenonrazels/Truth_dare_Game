from django import forms
from .models import Players

class PlayersForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = ['name', 'gender', 'ageType']

    # Override the gender and ageType fields
    gender = forms.ChoiceField(
        choices=[('', 'Select Gender')] + Players.GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})  # Add styling if needed
    )
    ageType = forms.ChoiceField(
        choices=[('', 'Select Age Type')] + Players.AGE_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})  # Add styling if needed
    )
