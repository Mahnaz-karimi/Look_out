from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from person.models import Profile


class UserRegisterForm(UserCreationForm):

    class Meta:  # meta classe giv os en nested namespace for configurations in i en plads
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):  # Opdateres user
    email = forms.EmailField()

    class Meta:
        model = User  # vil user bliver opdatet
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):  # Opdatere profile

    class Meta:
        model = Profile  # opdatere user-profile

        fields = ['image']  # opdateres kun billede for profilen. User vil opdates i ovenstående methode
