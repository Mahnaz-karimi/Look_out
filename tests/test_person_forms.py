from django.test import TestCase, Client
from person.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class TestForms(TestCase):

    def test_UserRegisterForm(self):
        form = UserRegisterForm(data={
            'username': 'username',
            'email': 'username@yahoo.com',
            'password1': 'tests123',
            'password2': 'tests123'
        })
        # print("print form : ", form)
        self.assertTrue(form.is_valid())

    def test_UserRegister_form_not_valid_one_pass(self):
        form = UserRegisterForm(data={
            'username': 'username',
            'password1': 'tests123',
            'email': 'username@yahoo.com'

        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)  # Der er en enkelt fejl

    def test_UserRegister_form_not_valid_without_mail(self):
        form = UserRegisterForm(data={
            'username': 'Mahn',
            'password1': 'madrese122',
            'password2': 'madrese122'

        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_UserRegister_form_not_valid_with_wrong_password(self):
        form = UserRegisterForm(data={
            'username': 'Mahnaz',
            'password1': 'Mahnaz1234',
            'password2': 'Mahnaz1234',
            'email': 'mahnaazi@yahoo.com'

        })
        self.assertFalse(form.is_valid())

    def test_UserRegister_form_not_valid_without_username(self):
        form = UserRegisterForm(data={
            'password1': 'madrese122',
            'password2': 'madrese122',
            'email': 'mahnaazi@yahoo.com'

        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)  # Her mangler vi en data for formen!

    def test_UserRegister_no_data(self):
        form = UserRegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)  # Der skulle være fire fejl fordi vi har ingen data

    def test_UserRegister_no_3_data(self):
        form = UserRegisterForm(data={'email': 'mahnaazi@yahoo.com'})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # der skulle være tre fejl fordi vi har givet en data

    def test_UserUpdateForm(self):
        form = UserUpdateForm(data={
            'username': 'Mahnaaaz',
            'email': 'newemail@ya.com',

        })
        self.assertTrue(form.is_valid())

    def test_UserUpdateForm_form_not_valid_mail(self):
        form = UserUpdateForm(data={
            'username': 'Mahnooo',
            'email': 'madrese122'
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_UserUpdateForm_form_not_valid_mail(self):
        form = UserUpdateForm(data={
            'username': '',
            'email': 'madrese122'
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def test_ProfileUpdateForm(self):
        form = ProfileUpdateForm(data={
            'image': 'default.jpg',

        })
        self.assertTrue(form.is_valid())

    def test_ProfileUpdateForm(self):
        form = ProfileUpdateForm(data={
            'image': 'default',

        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
