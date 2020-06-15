from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    password_re = forms.CharField()
    nickname = forms.CharField()
