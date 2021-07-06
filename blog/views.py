from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # mix in sikre os at user autorotiet
from blog.models import Post
from django.views.generic import (
    ListView,
    DetailView, # når vil kigges efter detail of post
    CreateView,
    UpdateView,
    DeleteView
)


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  # <app>/<model>_<viewtype>.html  PostListView.as_view() med den mens <app> / <model>_<vietype> html- app er ligsom vores repport app. model er database og vieetype er list.
    context_object_name = 'posts'
    ordering = ['-date_posted'] # med - vil nyeste post vil stå først