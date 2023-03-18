from django import urls
import pytest
from django.contrib.auth.models import User
from blog.models import Post, Comment, Photo, Youtube, Images
from blog.views import search
from django.test import RequestFactory

url_data = [
    ('person:login', 200),
    ('person:logout', 200),
    ('blog:photo-new', 302)
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
def test_photo_create_view(client, user_data_for_login, create_user_for_login, data_for_create_photo):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind
    user_url = urls.reverse('blog:photo-new')
    resp = client.post(user_url, data=data_for_create_photo)
    print("print form : ", str(resp))
    assert resp.status_code == 302  # redirect to home view efter at oprette en photo
    assert resp.url == urls.reverse('blog:blog-home')  # Efter create a photo, bliver man redirected til "/blog/" home


@pytest.mark.django_db
def test_photo_update_view(client, user_data_for_login, create_user_for_login, photo_data):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind
    photo = Photo.objects.latest('pk')
    user_url = urls.reverse('blog:photo-update', kwargs={'pk': photo.pk})
    resp = client.post(user_url, {
        'description': 'title',
        'image': 'default.jpg',
        'author': create_user_for_login,
        'category': photo.category,
    })
    print("PhotoUpdate: ", str(resp))
    assert resp.status_code == 302  # Redirect to home view efter at update en photo
    assert resp.url == urls.reverse('blog:blog-home')  # Efter update a photo, bliver man redirected til "/blog/"


@pytest.mark.django_db
def test_photo_delete_view(client, user_data_for_login, create_user_for_login, photo_data):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind
    print("data for foto", photo_data)
    photo = Photo.objects.latest('pk')
    user_url = urls.reverse('blog:photo-delete', kwargs={'pk': photo.id})
    resp = client.post(user_url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('blog:blog-home')


@pytest.mark.django_db
def test_photo_album_create_view(client, user_data_for_login, create_user_for_login, photo_data):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind fordi i youtube.html
    photo = Photo.objects.latest('pk')
    user_url = urls.reverse('blog:add-image-album', kwargs={'pk': photo.pk})
    resp = client.post(user_url, {
        'photo': photo,
        'description': 'title',
        'images': 'default.jpg',
        'author': create_user_for_login
    })
    print("print form : ", str(resp))
    assert resp.status_code == 302  # redirect to home view efter at oprette en photo
    assert resp.url == urls.reverse('blog:blog-home')  # Efter create a image for album, redirectes til home page


@pytest.mark.django_db
def test_image_album_delete_view(client, user_data_for_login, create_user_for_login, data_for_image_album):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind
    imageAlbum = Images.objects.latest('pk')
    user_url = urls.reverse('blog:photo-album-delete', kwargs={'pk': imageAlbum.id})
    resp = client.post(user_url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('blog:blog-home')


@pytest.mark.django_db
def test_post_create_view(client, user_data_for_login, create_user_for_login):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind
    user_url = urls.reverse('blog:post-new')
    resp = client.post(user_url, {         # en client får fat i den user-url og derefter sender de data med post method
        'title': 'Unit test post title 1',
        'content': 'Unit test post content 1',
    })
    print("PostCreate : ", str(resp))
    assert resp.status_code == 302  # redirect to home view efter at oprette en post
    assert resp.url == urls.reverse('blog:post-view')  # Efter create a Post, bliver man redirected til "/blog/" home


@pytest.mark.django_db
def test_post_update_view(client, user_data_for_login, create_user_for_login, post_data):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind
    post = Post.objects.latest('pk')
    user_url = urls.reverse('blog:post-update', kwargs={'pk': post.pk})  # Se comment under en post
    resp = client.post(user_url, {
        'title': 'title',
        'content': 'content'
    })
    assert resp.status_code == 302  # Redirect to home view efter at update en post
    assert resp.url == urls.reverse('blog:post-detail-view', kwargs={'pk': post.id})  # Efter update a Post, bliver man redirected til "/blog/"


@pytest.mark.django_db
def test_post_delete_view(client, user_data_for_login, create_user_for_login, post_data):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind
    post = Post.objects.latest('pk')
    user_url = urls.reverse('blog:post-delete', kwargs={'pk': post.id})
    resp = client.post(user_url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('blog:post-view')


@pytest.mark.django_db
def test_comment_new_post_create_view(client, user_data_for_login, create_user_for_login, post_data):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind
    post = Post.objects.latest('pk')
    user_url = urls.reverse('blog:comment-new', kwargs={'id': post.id})
    resp = client.post(user_url, {
        'content': 'content1'
    })
    assert resp.status_code == 302  # Redirect to home view efter at update en post
    assert resp.url == urls.reverse('blog:post-view')  # Efter update a Post, bliver man redirected til "/blog/"


@pytest.mark.django_db
def test_comment_delete_view(client, user_data_for_login, create_user_for_login, comment_data):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind
    comment = Comment.objects.latest('pk')
    user_url = urls.reverse('blog:comment-delete', kwargs={'pk': comment.id})
    resp = client.post(user_url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('blog:post-view')


@pytest.mark.django_db
def test_comment_delete_view_with_other_user(client, user_data_for_login, create_user_for_login, comment_data2):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind
    comment = Comment.objects.latest('pk')
    user_url = urls.reverse('blog:comment-delete', kwargs={'pk': comment.id})
    resp = client.post(user_url)
    assert resp.status_code == 403


@pytest.mark.django_db
def test_post_comments_view(client, create_user_for_login, post_data):
    post = Post.objects.latest('pk')
    user_url = urls.reverse('blog:post-comments', kwargs={'id': post.id})  # Se komments under en post
    resp = client.get(user_url)
    assert resp.status_code == 200  # Fordi vi bliver ikke redirectet
    assert "Go back" in str(resp.content)


@pytest.mark.django_db
def test_user_post_list_view(client, create_user_for_login):
    user = User.objects.latest('pk')
    user_url = urls.reverse('blog:user-posts', kwargs={'username': user.username})  # Se post under en user
    resp = client.get(user_url)
    assert resp.status_code == 200  # Fordi vi er logget ind bliver vi ikke redirectet
    assert "Tibage til hovedsiden" in str(resp.content)


@pytest.mark.django_db
def test_youtube_create_view(client, user_data_for_login, create_user_for_login, data_for_youtube):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind fordi i youtube.html
    user_url = urls.reverse('blog:youtube-new')
    resp = client.post(user_url, data=data_for_youtube)
    print("print form : ", str(resp))
    assert resp.status_code == 302  # redirect to home view efter at oprette en photo
    assert resp.url == urls.reverse('blog:youtube-videos')  # Efter create a photo, bliver man redirected til "/blog/" home


@pytest.mark.django_db
def test_youtube_delete_view(client, user_data_for_login, create_user_for_login, data_youtube):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind
    youtube = Youtube.objects.latest('pk')
    user_url = urls.reverse('blog:youtube-delete', kwargs={'pk': youtube.id})
    resp = client.post(user_url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('blog:youtube-videos')


@pytest.mark.django_db
def test_search(client, user_data_for_login, create_user_for_login, post_data):
    factory = RequestFactory()
    request = factory.post('blog:search', data={'search': 'title1'})
    response = search(request)
    assert response.status_code == 200
    assert 'Alle Post' in str(response.content)
    assert bytes('title1', 'utf-8') in response.content
