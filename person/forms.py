from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from person.models import Profile


class UserRegisterForm(UserCreationForm):

    class Meta:  # meta classe giv os en nested namespace for configurations in i en plads
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm): # den form dukkes up ind i users profilens side og vil opdates username og email
    email = forms.EmailField()

    class Meta:
        model = User  # det model vil vi arbjede med vil vil kaldes
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm): # den method vil opdatere image
    class Meta:
        model = Profile  # den model vi bruger her er  profile model. så derfor skriver vi under 2 methode og derefter
        # kalder vi dem under views.py for at de kan opdatere userprofile
        fields = ['image']
