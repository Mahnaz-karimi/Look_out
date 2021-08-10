from blog.models import Post, Comment, Photo
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, CreateView, DeleteView, UpdateView
)
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # mix in sikre os at user er logget ind
import config.settings
from django.shortcuts import redirect


class PhotoListView(ListView):
    model = Photo
    template_name = 'blog/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'photos'
    # ordering = ['-date_posted']  # med - vil nyeste post vil stå først
    paginate_by = config.settings.PAGINATION_COUNT


class PostListView(ListView):
    model = Post
    template_name = 'blog/post.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # med - vil nyeste post vil stå først
    paginate_by = config.settings.PAGINATION_COUNT


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):  # tilføje logind-brugeren som author in i post
        form.instance.author = self.request.user  # adder den aktuelle user til formen
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            try:
                title = request.POST['title']
                content = request.POST['content']
                description = request.POST['description']
                images = request.FILES.getlist('images')
                post = Post.objects.create(title=title, content=content, author=self.request.user)
                post.save()
                for image in images:
                    photo = Photo.objects.create(
                        post=post,
                        image=image,
                        description=description
                    )
                    photo.save()
                return redirect('blog:blog-home')
            except():
                return redirect('blog:post-new')


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # Mixin bruges til sikre og skal stå først
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # testMixin teste at brugeren som har logget ind er lige med postens author
        post = self.get_object()
        if self.request.user == post.author:  # tjekke at den post user is log in
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'  # efter delete a object så vil redirect brugeren til home side

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentNewPostCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    success_url = '/blog/'

    def form_valid(self, form):  # tilføje logind-brugeren som author in i post
        post = get_object_or_404(Post, id=self.kwargs['id'])
        form.instance.post = post
        form.instance.author = self.request.user  # tjekker at den er aktuelle user
        return super(CommentNewPostCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):  # context bliver den valgte post
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['id'])
        context['post'] = Post.objects.get(id=post.id)
        return context


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/blog/'  # efter delete a object så vil redirect brugeren til home side

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCommentsView(ListView):
    model = Comment
    template_name = 'blog/post_comments.html'

    def get_context_data(self, **kwargs):  # tag post-id og retunere data
        context = super(PostCommentsView, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['id'])
        context = {'comments': Comment.objects.filter(post=post.id)}
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = config.settings.PAGINATION_COUNT

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_posted')
