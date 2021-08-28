from django import forms


class WizardForm(forms.Form):
    name = forms.CharField(max_length=45, min_length=4)
    pet = forms.CharField(max_length=45, min_length=4)
    house_id = forms.IntegerField(min_value=1)
    year = forms.IntegerField(min_value=1)
