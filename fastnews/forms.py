from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    password_re = forms.CharField()
    nickname = forms.CharField()


class MyAccountForm(forms.Form):
    now_password = forms.CharField()
    new_password = forms.CharField(required=False)
    nickname = forms.CharField()
