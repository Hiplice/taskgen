from django import forms


def get_post_data(fields, request):
    data = {}

    for field in fields:
        data[field] = request.POST.get(field)

    return data


class AuthForm(forms.Form):
    login = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=50)

    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=30)