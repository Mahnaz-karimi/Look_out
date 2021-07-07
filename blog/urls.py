from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from blog.views import (
    PostListView,
LoginView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'),
         name='logout'),
]
