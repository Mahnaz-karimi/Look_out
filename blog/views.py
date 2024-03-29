from blog.models import Post, Comment, Photo, Youtube, Images
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
)
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # mix in sikre os at user er logget ind
import config.settings
from django.shortcuts import redirect


# Photos detail
class PhotoAlbumDetailView(TemplateView):
    template_name = "blog/album_detail.html"
    paginate_by = config.settings.PAGINATION_COUNT

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photodetail'] = Photo.objects.get(id=self.kwargs['pk'])
        return context


# add images to album
class AddImage_AlbumView(LoginRequiredMixin, TemplateView):
    template_name = "blog/add_photo_album.html"
    success_url = reverse_lazy('blog:blog-home')

    def post(self, request, *args, **kwargs):
        try:
            images = request.FILES.getlist('images')
            photo = Photo.objects.get(id=self.kwargs['pk'])
            for image in images:
                Images.objects.create(author=self.request.user, photo=photo, images=image)
            return redirect('blog:blog-home')
        except():
            return redirect('blog:post-new')


# delete image of album
class ImageAlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Images
    success_url = reverse_lazy(
        'blog:blog-home')  # efter delete a image af albume så vil redirect brugeren til home side
    template_name = "blog/album_delete_photo.html"

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.author:
            return True
        return False


class YoutubeListView(ListView):
    model = Youtube
    template_name = 'blog/youtube.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'youtubes'
    paginate_by = config.settings.PAGINATION_COUNT


class YoutubeCreateView(LoginRequiredMixin, CreateView):
    model = Youtube
    fields = ['content', 'video']
    template_name = 'blog/youtube_form.html'
    success_url = '/blog/youtube/videos'

    def form_valid(self, form):  # tilføje logind-brugeren som author in i post
        form.instance.author = self.request.user  # adder den aktuelle user til formen
        return super().form_valid(form)


class YoutubeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Youtube
    success_url = '/blog/youtube/videos'  # efter delete a object så vil redirect to the url

    def test_func(self):
        Youtube = self.get_object()
        if self.request.user == Youtube.author:
            return True
        return False


class PhotoListView(ListView):
    model = Photo
    template_name = 'blog/gallery.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'photos'
    paginate_by = config.settings.PAGINATION_COUNT


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['description']
    template_name = 'blog/photo_form.html'
    success_url = '/blog/'
    context_object_name = 'photos'

    def form_valid(self, form):  # tilføje logind-brugeren som author in i post
        form.instance.author = self.request.user  # adder den aktuelle user til formen
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):  # save pictures
        if request.method == 'POST':
            try:
                description = request.POST['description']
                images = request.FILES.getlist('images')
                for image in images:
                    Photo.objects.create(image=image, description=description,
                                         author=self.request.user)
                return redirect('blog:blog-home')
            except():
                return redirect('blog:post-new')


class PhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # Mixin bruges til sikre og skal stå først
    model = Photo
    fields = ['image', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # testMixin teste at brugeren som har logget ind er lige med postens author
        photo = self.get_object()
        if self.request.user == photo.author:  # tjekke at den post user is log in
            return True
        return False


class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    success_url = '/blog/'  # efter delete a object så vil redirect brugeren til home side

    def test_func(self):
        photo = self.get_object()
        if self.request.user == photo.author:
            return True
        return False


class PostListView(ListView):
    model = Post
    template_name = 'blog/post.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # med - vil nyeste post vil stå først
    paginate_by = config.settings.PAGINATION_COUNT


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/blog/posts/'
    template_name = 'blog/post_form.html'

    def form_valid(self, form):  # tilføje logind-brugeren som author in i post
        form.instance.author = self.request.user  # adder den aktuelle user til formen
        return super().form_valid(form)


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
    success_url = '/blog/posts/'  # efter delete a object så vil redirect brugeren til home side

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentNewPostCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    success_url = '/blog/posts/'

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
    success_url = '/blog/posts/'  # efter delete a object så vil redirect brugeren til home side

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


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = config.settings.PAGINATION_COUNT

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_posted')
