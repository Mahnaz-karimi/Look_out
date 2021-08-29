from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  # Finde tid som en post bliver gemt
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Post bliver forbundet med user med foreignkey.
    #  on_delete gøre at hvis en bruger bliver slettet så vil posten bliver også slettet. den gøres med Cascade
    #  med store bogstaver

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog-home')  # reverse vil return the full path as a string url pattern


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=False, blank=False)
    image = models.FileField(null=False, blank=False, upload_to='profile_pics/%Y/%m/%d')
    description = models.TextField()

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('blog:blog-home')  # reverse vil return the full path as a string url pattern

    class Meta:
        ordering = ['id']


class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # on_delete gøre at hvis en bruger bliver slettet
    # så vil posten bliver også slettet. den gøres med Cascade med store bogstaver
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")

    def __str__(self):
        return self.author.username
