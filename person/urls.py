from person.views import register
from django.urls import path
from person.views import profile


urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]
