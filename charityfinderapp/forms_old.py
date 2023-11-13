from django import forms


class CharityForm(forms.Form):
    charity_name = forms.CharField()
    street_name = forms.CharField()
    post_code = forms.CharField()
    district_name = forms.CharField()
    contact_number = forms.CharField()
    extra_info = forms.CharField(required=False)
