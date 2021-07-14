from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:  # meta classe giv os en nested namespace for configurations in i en plads
        model = User
        fields = ['username', 'email', 'password1', 'password2']