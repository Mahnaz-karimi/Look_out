from django import urls
from django.contrib.auth import get_user_model
import pytest


# Data til data-drevet test
url_data = [
    ('person:register', 200),
    ('person:profile', 302),
]


@pytest.mark.parametrize("url, expected", url_data)  # url er adressen og expected er response-kode i url_data
def test_logged_views(client, url, expected):
    temp_url = urls.reverse(url)
    resp = client.get(temp_url)  # Client er som en browser som vil bruge urlen
    assert resp.status_code == expected  # Når man ikke er logget ind så vil de redirect til login-side


@pytest.mark.django_db
def test_person_register(client, user_data_for_login, create_user_for_login, user_data_for_register):
    user_model = get_user_model()
    assert user_model.objects.count() == 1  # Når vi kalder create_user_model in i modelen opreetter vi en user
    login_url = urls.reverse('blog:login')
    resp = client.post(login_url, data=user_data_for_login)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('blog:blog-home')  # Når man logger ind så bliver man redirected til "/case/"
    register_url = urls.reverse('person:register')  # Vi vil registere en ny bruger efter vi har logget ind
    response = client.post(register_url, user_data_for_register)
    assert user_model.objects.count() == 2  # Ny bruger bliver rigistered så skal være 2 bruger ind i database
    assert response.status_code == 302
    assert response.url == urls.reverse('blog:blog-home')


@pytest.mark.django_db
def test_person_profile(client, user_data_for_login, create_user_for_login, user_data_for_register):
    user_model = get_user_model()
    assert user_model.objects.count() == 1  # Når vi kalder create_user_model in i modelen opreetter vi en user
    login_url = urls.reverse('blog:login')
    resp = client.post(login_url, data=user_data_for_login)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('blog:blog-home')  # Når man logger ind så bliver man redirected til "/case/"
    profile_url = urls.reverse('person:profile')  # Vi vil registere en ny bruger efter vi har logget ind
    response = client.post(profile_url)
    assert response.status_code == 200
