from django.urls import path
from blog.views import (
    PostListView,
    PostCommentsView,
    UserPostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='post-new'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:id>/comments/', PostCommentsView.as_view(), name='post-comments'),
    path('user/posts/<str:username>', UserPostListView.as_view(), name='user-posts'),
]
