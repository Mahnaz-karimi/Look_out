from person.views import register, profile
from django.urls import path


app_name = 'person'
urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]
