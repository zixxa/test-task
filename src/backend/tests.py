from django.test import TestCase
from src.backend.models import User, Profile
from src.backend.forms import ProfileList

class ProfilesTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='Олег', password='Qwerty123')
        self.user2 = User.objects.create_user(username='Николай', password='Qwerty123')
        self.user3 = User.objects.create_user(username='Евгений', password='Qwerty123')

        self.sender = Profile.objects.create(user=self.user1, inn='100000000000', check=2000.00)
        self.receiver1 = Profile.objects.create(user=self.user2, inn='200000000000', check=2000.00)
        self.receiver2 = Profile.objects.create(user=self.user3, inn='030000000000', check=2000.00)

    def test_form(self):
        data = {
            'user': 'Олег',
            'innset': '200000000000 030000000000',
            'check': '100'
        }
        form = ProfileList(data)
        self.assertTrue(form.is_valid)

    def test_view(self):
        data = {
            'user': 'Олег',
            'innset': '200000000000 030000000000',
            'check': '100'
        }
        response = self.client.post('/',data)
        self.assertEqual(response.status_code, 200)

