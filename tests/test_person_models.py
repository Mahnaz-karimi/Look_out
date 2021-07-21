from person.models import Profile
from django.contrib.auth.models import User
from django.test import TestCase


class PersonModelTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='1jacob11', email='jacob@…', password='top_secret')
        self.profile = Profile.objects.get(user=self.user)

    # Profile has user
    def test_Profile_has_user(self):
        self.assertEqual(self.profile.user.username, self.user.username)

    def test_Profile_has_image(self):
        self.assertEqual(self.profile.image, 'default.jpg')
