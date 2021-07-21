from django import urls
import pytest
from django.contrib.auth import get_user_model

url_data = [
    ('blog:login', 200),
    ('blog:logout', 200),
]


@pytest.mark.parametrize("url, expected", url_data)
def test_post_views(client, url, expected):
    temp_url = urls.reverse(url)
    resp = client.get(temp_url)
    assert resp.status_code == expected


@pytest.mark.django_db
def test_user_login(client, user_data_for_login, create_user_for_login):
    user_model = get_user_model()
    assert user_model.objects.count() == 1  # Når vi kalder create_user_model in i modelen opreetter vi en user
    login_url = urls.reverse('blog:login')
    resp = client.post(login_url, data=user_data_for_login)  # Her poster en login-data til login-side
    assert resp.status_code == 302
    assert resp.url == urls.reverse('blog:blog-home')  # Når man logger ind så bliver man redirected til "/blog/"


@pytest.mark.django_db
def test_PostCommentsView(client, post_data, comment_data):
    post = post_data
    user_url = urls.reverse('blog:post-comments', kwargs={'id': post.id})  # Se sagerne under en sagsinfo
    resp = client.get(user_url)
    assert resp.status_code == 200  # Fordi vi er logget ind bliver vi ikke redirectet
    assert "Go back" in str(resp.content)


@pytest.mark.django_db
def test_UserPostListView(client, post_data):
    post = post_data
    user_url = urls.reverse('blog:user-posts', kwargs={'username': post.author.username})  # Se sagerne under en sagsinfo
    resp = client.get(user_url)
    assert resp.status_code == 200  # Fordi vi er logget ind bliver vi ikke redirectet
    assert "Tibage til hovedsiden" in str(resp.content)
