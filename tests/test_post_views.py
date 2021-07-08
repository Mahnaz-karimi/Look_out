from django import urls
from django.contrib.auth import get_user_model
import pytest


url_data = [
    ('blog:login', 200),
    ('blog:logout', 200),
]


@pytest.mark.parametrize("url, expected", url_data)
def test_post_views(client, url, expected):
    temp_url = urls.reverse(url)
    resp = client.get(temp_url)
    assert resp.status_code == expected
