from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.test import TestCase


# Create your tests here.
class CheckLogin(TestCase):

    def setUp(self) -> None:
        new_user = User.objects.create_user(username='temp@mail.ru', email='temp@mail.ru', password='secret')
        new_user.save()

    def test_login_works(self):
        user = authenticate(username='temp@mail.ru', password='secret')
        self.assertIsNotNone(user, msg="Can not authenticate user!")

    def test_change_password_works(self):
        new_user = User.objects.get(username='temp@mail.ru')
        new_user.set_password('secret2')
        new_user.set_password('secret')

    def tearDown(self) -> None:
        new_user = User.objects.get(username='temp@mail.ru')
        new_user.delete()


class CheckSendingEmail(TestCase):
    def test_sending_email(self):
        status = send_mail(
            subject="Test message",
            message="Test message",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['arsl.sh056@mail.ru', ],
        )

        self.assertEqual(status, 1, f"send_mail sent only {status} message, but should send 1.")
