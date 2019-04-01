import datetime

from django import forms

class ClientForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
