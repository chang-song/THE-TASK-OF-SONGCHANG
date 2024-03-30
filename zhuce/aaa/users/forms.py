from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class AuthorizationCodeForm(forms.Form):
    authorization_code = forms.CharField()
