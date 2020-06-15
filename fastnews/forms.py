from django import forms


class WriteComment(forms.Form):
    content = forms.CharField()


class WriteDebateForm(forms.Form):
    debate_name = forms.CharField()


class WriteArticleForm(forms.Form):
    category = forms.CharField()
    title = forms.CharField()
    content = forms.CharField()


class SettlementForm(forms.Form):
    bank_code = forms.CharField()
    account_number = forms.CharField()
    real_name = forms.CharField()


class MyAccountForm(forms.Form):
    now_password = forms.CharField()
    new_password = forms.CharField(required=False)
    nickname = forms.CharField()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    password_re = forms.CharField()
    nickname = forms.CharField()
