from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(help_text="temp@mail.ru")
    password = forms.PasswordInput()
