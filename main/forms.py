from .models import user
from django.forms import ModelForm, TextInput, PasswordInput

class userform(ModelForm):
    class Meta:
        model = user
        fields = ['name', 'surname', 'login', 'password']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': "name",
                'class':"form-control",
                'id':"floatingInput"
            }),
            'surname': TextInput(attrs={
                'placeholder': "surname",
                'class': "form-control",
                'id': "floatingInput"
            }),
            'login': TextInput(attrs={
                'placeholder': "login",
                'class': "form-control",
                'id': "floatingInput"
            }),
            'password': TextInput(attrs={
                'placeholder': "password",
                'class': "form-control",
                'id': "floatingInput"
            })
        }


class entrform(ModelForm):
    class Meta:
        model = user
        fields = ['login', 'password']

        widgets = {
            'login': TextInput(attrs={
                'placeholder': "login",
                'class': "form-control",
                'id': "floatingInput"
            }),
            'password': TextInput(attrs={
                'placeholder': "password",
                'class': "form-control",
                'id': "floatingInput"
            })
        }