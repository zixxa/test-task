from django.test import TestCase
from src.backend.models import User, Profile
from src.backend.views import index
from src.backend.forms import ProductList

class ItemsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Олег', password1='Qwerty123', password2='Qwerty123)
        self.user2 = User.objects.create(username='Николай', password1='Qwerty123', password2='Qwerty123)
        self.user3 = User.objects.create(username='Евгений', password1='Qwerty123', password2='Qwerty123)

        self.sender = Profile.objects.create(user=self.user1, inn=100000000, check=2000.00)
        self.receiver1 = Profile.objects.create(user=self.user2, inn=200000000, check=2000.00)
        self.receiver2 = Profile.objects.create(user=self.user3, inn=030000000, check=2000.00)

    def test_form(self):
    form_data = {'user':self.profile.user, 'innset':self.profile, 'check':1000}


    def test_profiles(self):
        index()
        self.assertIn
