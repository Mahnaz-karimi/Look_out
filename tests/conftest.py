import pytest
from django.contrib.auth import get_user_model
from blog.models import Post, Comment, Photo, Category, Youtube, Images
from django.conf import settings
from django.contrib.auth.models import User

# Test med toggle-feature enabled
settings.FEATURES['REVISIT_CASE'] = True


@pytest.fixture
def user_data_for_register():
    return {
        'username': '12username',
        'password1': 'my_password123',
        'password2': 'my_password123',
        'email': 'username@yahoo.com'
    }


@pytest.fixture
def data_for_create_photo():
    return {
        'image': 'default.jpg',
        'description': 'pictures'
    }


@pytest.fixture
def user_data_for_login():
    return {'username': 'user_name', 'password': 'tests123'}


@pytest.fixture
def data_for_youtube():
    return {
        'content': 'test',
        'video': 'https://www.youtube.com/watch?v=Geq60OVyBPg&t=8s'
    }


@pytest.fixture
def data_youtube():
    author = User.objects.latest('pk')
    youtube = Youtube.objects.create(content='test', video='https://www.youtube.com/watch?v=Geq60OVyBPg&t=8s', author=author)
    return youtube


@pytest.fixture
def data_for_image_album():
    author = User.objects.latest('pk')
    category = Category.objects.create(name="Ny")
    photo = Photo.objects.create(author=author, image='default.jpg', description='test', category=category)
    image = Images.objects.create(description='test', photo=photo, images='default.jpg', author=author)
    return image


@pytest.fixture
def create_user_for_login(user_data_for_login):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data_for_login)
    return test_user


@pytest.fixture
def post_data():
    title = "title1"
    content = 'post_content_Test1'
    author = User.objects.latest('pk')
    post = Post.objects.create(title=title, content=content, author=author)
    return post


@pytest.fixture
def photo_data():
    author = User.objects.latest('pk')
    category = Category.objects.create(name="Ny")
    photo = Photo.objects.create(author=author, image='default.jpg', description='test', category=category)
    return photo


@pytest.fixture
def comment_data():
    content = 'post_content_Test'
    author = User.objects.latest('pk')
    post = Post.objects.create(title="title2", content=content, author=author)
    comment = Comment.objects.create(content='comment_content_Test2', author=author, post=post)
    return comment


@pytest.fixture
def comment_data2():
    content = 'post_content_Test'
    author = User.objects.create(username="newuser", password="test123", email="test@test.dk")
    post = Post.objects.create(title="title2", content=content, author=author)
    comment = Comment.objects.create(content='comment_content_Test2', author=author, post=post)
    return comment
