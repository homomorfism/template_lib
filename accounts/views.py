from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from accounts.forms import LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout

# Create your views here.

# TODO add templates for login and implement login_view
# Make assert that user is not registered at this moment
from category.models import Category


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(email=email, password=password)

            if user is not None:
                return HttpResponseRedirect(redirect_to='/home/')

    else:
        form = LoginForm()

    return render(request, 'form.html', context={
        "categories": Category.objects.all(),
        'form': form,
    })


# TODO implement logout_view
# TODO доделать!
@login_required(redirect_field_name='login')
def logout_view(request):
    logout(request)
    pass


# TODO add templates for changing password and implement change_password_view
@login_required(redirect_field_name='login')
def change_password_view(request):
    pass


# TODO add templates for reset password and implement reset_password_view
def reset_password_view(request):
    pass


def sign_up_view(request):
    pass