import pytest
from django.contrib.auth import get_user_model
from blog.models import Post, Comment
from django.conf import settings


# Test med toggle-feature enabled
settings.FEATURES['REVISIT_CASE'] = True


@pytest.fixture
def user_data_for_register():
    return {
        'username': 'my_username',
        'password1': 'my_password123',
        'password2': 'my_password123',
        'email': 'username@yahoo.com'
    }


@pytest.fixture
def user_data_for_login():
    return {'username': 'user_name', 'password': 'tests123'}


@pytest.fixture
def create_user_for_login(user_data_for_login):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data_for_login)
    return test_user


@pytest.fixture
def post_data():
    content = Post.objects.create(name='post_content_Test')
    user_model = get_user_model()
    author = user_model.objects.create_user(**user_data_for_register)
    post = Post.objects.create(content=content, author=author)
    return post


@pytest.fixture
def comment_data():
    content = Post.objects.create(name='post_content_Test')
    user_model = get_user_model()
    author = user_model.objects.create_user(**user_data_for_register)
    post = Post.objects.create(content=content, author=author)
    comment = Comment.objects.create(content='comment_content_Test', author=author, post=post)
    return post, comment
