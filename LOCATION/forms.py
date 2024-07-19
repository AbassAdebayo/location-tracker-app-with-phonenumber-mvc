from django import forms

class TrackForm(forms.Form):
    phone_number = forms.CharField(max_length=15, required=True)