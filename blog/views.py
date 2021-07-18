from blog.models import Post, Comment
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
)
from django.contrib.auth import views as auth_views
from django.shortcuts import get_object_or_404


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  # <app>/<model>_<viewtype>.html  PostListView.as_view() med den mens <app> / <model>_<vietype> html- app er ligsom vores repport app. model er database og vieetype er list.
    context_object_name = 'posts'
    ordering = ['-date_posted']  # med - vil nyeste post vil stå først


class LoginView(auth_views.LoginView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostCommentsView(ListView):
    model = Comment
    template_name = 'blog/post_comments.html'

    def get_context_data(self, **kwargs):
        context = super(PostCommentsView, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['id'])
        context = {'comments': Comment.objects.filter(post=post.id)}
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_posted')
