from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import CustomeUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=128, label="Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label="Mot de passe")


class CustomerSignupForm(UserCreationForm):
    class Meta:
        model = CustomeUser
        fields = UserCreationForm.Meta.fields