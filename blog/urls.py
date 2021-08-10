from django.urls import path
from blog.views import (
    PostListView,
    PostCommentsView,
    UserPostListView,
    PhotoCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentNewPostCreateView,
    CommentDeleteView
)

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PhotoCreateView.as_view(), name='post-new'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/comments/<int:id>/', PostCommentsView.as_view(), name='post-comments'),
    path('user/posts/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/comments/<int:id>/', CommentNewPostCreateView.as_view(), name='comment-new'),
    path('delete/comments/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
]
