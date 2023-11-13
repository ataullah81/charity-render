from django import forms

from charityfinderapp.models import Charityinformation


class CharityForm(forms.ModelForm):
    class Meta:
        model = Charityinformation
        fields = "__all__"


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
