from django import forms


class AuthForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=30)

    username = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=50)