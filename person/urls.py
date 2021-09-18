from person.views import register, profile, view
from django.urls import path
from person.views import LoginView
from django.contrib.auth import views as auth_views

app_name = 'person'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='person/login.html'), name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='person/logout.html'),
         name='logout'),
    path('adminlte/', view, name='adminlte'),
]
