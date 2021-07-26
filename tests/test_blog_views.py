from django import urls
import pytest
from django.contrib.auth.models import User
from blog.views import Post
url_data = [
    ('person:login', 200),
    ('person:logout', 200),
    ('blog:post-new', 302)
]


@pytest.mark.parametrize("url, expected", url_data)
def test_post_views(client, url, expected):
    temp_url = urls.reverse(url)
    resp = client.get(temp_url)
    assert resp.status_code == expected


@pytest.mark.django_db
def test_user_login(client, user_data_for_login, create_user_for_login):
    login_url = urls.reverse('person:login')
    resp = client.post(login_url, data=user_data_for_login)  # Her poster en login-data til login-side
    assert resp.status_code == 302
    assert resp.url == urls.reverse('blog:blog-home')  # Når man logger ind så bliver man redirected til "/blog/"


@pytest.mark.django_db
def test_PostCreateView(client, user_data_for_login, create_user_for_login):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind
    user_url = urls.reverse('blog:post-new')
    resp = client.post(user_url, {          # tIlføjes en post
        'title': 'Unit test post title 1',
        'content': 'Unit test post content 1',
        'author': create_user_for_login
    })
    assert resp.status_code == 302  # redirect to home view efter at oprette en post
    assert resp.url == urls.reverse('blog:blog-home')  # Efter create a Post, bliver man redirected til "/blog/" home


@pytest.mark.django_db
def test_PostUpdateView(client, user_data_for_login, create_user_for_login, post_data):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind
    post = Post.objects.latest('pk')
    user_url = urls.reverse('blog:post-update', kwargs={'pk': post.pk})  # Se comment under en post
    resp = client.post(user_url, {
        'title': 'title',
        'content': 'content'
    })
    assert resp.status_code == 302  # Redirect to home view efter at update en post
    assert resp.url == urls.reverse('blog:blog-home')  # Efter update a Post, bliver man redirected til "/blog/"


@pytest.mark.django_db
def test_PostCommentsView(client, comment_data):
    post = Post.objects.latest('pk')
    user_url = urls.reverse('blog:post-comments', kwargs={'id': post.id})  # Se comment under en post
    resp = client.get(user_url)
    assert resp.status_code == 200  # Fordi vi er logget ind bliver vi ikke redirectet
    assert "Go back" in str(resp.content)


@pytest.mark.django_db
def test_UserPostListView(client, create_user_for_login):
    user = User.objects.latest('pk')
    user_url = urls.reverse('blog:user-posts', kwargs={'username': user.username})  # Se sagerne under en sagsinfo
    resp = client.get(user_url)
    assert resp.status_code == 200  # Fordi vi er logget ind bliver vi ikke redirectet
    assert "Tibage til hovedsiden" in str(resp.content)
