from django import forms

# In future add possibility that entering by email or username

# For login to website
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.EmailField(help_text="temp@mail.ru")
    password = forms.PasswordInput()


# For changing password to another (old + new + repeat new)
# Assert that user is logged in now
class ChangePasswordForm(forms.Form):
    old_password = forms.PasswordInput()
    new_password = forms.PasswordInput()
    repeat_new_password = forms.PasswordInput()

    def clean_old_password(self):
        # TODO how to check that this password is correct?
        pass


# For Signing Up (registering)
class SignUpForm(forms.Form):
    email = forms.CharField(max_length=50, help_text="t@mail.ru")
    password = forms.PasswordInput()

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise ValidationError(f'Email: {email} is already in use!')

        else:
            return email


# For resetting password (via email)
class ResetPasswordForm(forms.Form):
    email = forms.CharField(max_length=50, help_text="Enter email of account")

    def clean_email(self):
        email = self.cleaned_data['email']

        # If email not exists -> raise error
        if not User.objects.filter(email=email).exists():
            raise ValidationError(f'Email: {email} is not in use!')

        else:
            return email
