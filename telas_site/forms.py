from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Resenha, Review, Usuario 

from django import forms

from django.forms.widgets import PasswordInput, TextInput

from django import forms


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Resenha
        fields = ['titulo_resenha', 'texto_resenha', 'nota_resenha']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['imagem_perfil']