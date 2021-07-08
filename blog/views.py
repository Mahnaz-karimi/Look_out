from blog.models import Post
from django.views.generic import (
    ListView,
)
from django.contrib.auth import views as auth_views

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  # <app>/<model>_<viewtype>.html  PostListView.as_view() med den mens <app> / <model>_<vietype> html- app er ligsom vores repport app. model er database og vieetype er list.
    context_object_name = 'posts'
    ordering = ['-date_posted']  # med - vil nyeste post vil stå først


class LoginView(auth_views.LoginView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context