from django.urls import path
from django.contrib.auth import views as auth_views

from blog.views import (
    PostListView,
    LoginView,
    PostCommentsView,
    UserPostListView,

)

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'),
         name='logout'),
    path('post/<int:id>/comments/', PostCommentsView.as_view(), name='post-comments'),
    path('user/posts/<str:username>', UserPostListView.as_view(), name='user-posts'),
]
