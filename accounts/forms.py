from django import forms

# In future add possibility that entering by email or username

# For login to website
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


# For changing password to another (old + new + repeat new)
# Assert that user is logged in now
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    new_password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    repeat_new_password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean_repeat_new_password(self):
        new_password = self.cleaned_data['new_password']
        repeat_new_password = self.cleaned_data['repeat_new_password']

        if new_password != repeat_new_password:
            raise ValidationError("New passwords should be matched!")
        else:
            return repeat_new_password


# For Signing Up (registering)
class SignUpForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    repeat_password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise ValidationError(f'Email: {email} is already in use!')

        else:
            return email

    def clean_repeat_password(self):
        password = self.cleaned_data['password']
        repeat_password = self.cleaned_data['repeat_password']

        if password != repeat_password:
            raise ValidationError("New passwords should be matched!")
        else:
            return repeat_password


# For resetting password (via email)
class ResetPasswordForm(forms.Form):
    email = forms.EmailField(max_length=50, help_text="Your email")

    def clean_email(self):
        email = self.cleaned_data['email']

        # If email not exists -> raise error
        if not User.objects.filter(email=email).exists():
            raise ValidationError(f'Email: {email} is not in use!')

        else:
            return email
