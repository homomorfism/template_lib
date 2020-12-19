import logging
import smtplib

from django.conf import settings
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from accounts.forms import LoginForm, ChangePasswordForm, SignUpForm, ResetPasswordForm
# Make assert that user is not registered at this moment
from category.models import Category


# Create your views here.

# Email = username
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)
            print(f"Email: {email}, password: {password}")
            if user is not None:
                login(request, user)
                return redirect(to='home')
            else:
                return render(request, 'login.html', context={
                    "categories": Category.objects.all(),
                    'form': form,
                    'type': 'error',
                    'message': "Authentication is failed, please use another email/password",
                })

    else:
        form = LoginForm()

    return render(request, 'login.html', context={
        "categories": Category.objects.all(),
        'form': form,
    })


@login_required(redirect_field_name='login')
def logout_view(request):
    logout(request)

    return redirect(to='home')


# TODO add templates for changing password and implement change_password_view
@login_required(redirect_field_name='login')
def change_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)

        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            repeat_new_password = form.cleaned_data['repeat_new_password']

            # Checks were made in forms.py, just to make sure
            assert (new_password == repeat_new_password)

            user = authenticate(username=request.user.username, password=old_password)

            if user is not None:
                # User with this credentials exists
                user.set_password(new_password)
                return render(request, 'change_password.html', context={
                    "categories": Category.objects.all(),
                    'form': form,
                    'type': 'success',
                    'message': "The password successfully changed!",
                })

            else:
                # User does not exists
                return render(request, 'change_password.html', context={
                    "categories": Category.objects.all(),
                    'form': form,
                    'type': 'error',
                    'message': "Your old password does not match with one we have!",
                })

    else:
        form = ChangePasswordForm()

    return render(request, 'change_password.html', context={
        "categories": Category.objects.all(),
        'form': form,
    })


def reset_password_view(request):
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            new_password = BaseUserManager().make_random_password(length=20)

            user = User.objects.get(email=email)
            user.set_password(new_password)

            try:
                text_message = \
                    f"Hello! You have requested form for changing password\n" \
                    f"Your new credentials: email={email}, password={new_password}\n" \
                    f"Use it to login to website"

                send_mail(
                    subject="Changing password at website.com",
                    message=text_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email, ],
                )

                logging.info(f"User={email} have requested to reset password, now password={new_password}")

                return render(request, 'reset_password.html', {
                    'categories': Category.objects.all(),
                    'form': form,
                    'message': "Your password were reset, please check your email :)",
                })
            except smtplib.SMTPException as e:
                logging.error(f"Can not send mail with resetting password to {email}")

                return render(request, 'reset_password.html', {
                    'categories': Category.objects.all(),
                    'form': form,
                    'message': f"Can not send mail with resetting password to {email}, try again please :( ",
                })

    else:
        form = ResetPasswordForm()

    return render(request, 'reset_password.html', {
        'categories': Category.objects.all(),
        'form': form,
    })


def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = BaseUserManager().make_random_password(length=20)

            text_message = \
                f"Hello! You can use your credentials in order to access the website:\n" \
                f"Email: {email}, generated password: {password}\n" \
                f"You can use it to login to website"

            try:
                send_mail(
                    subject=f"Registration to Shamil Library!",
                    message=text_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email, ]
                )
                logging.info(f"Confirmation letter to {email} were sent")
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()

                logging.info(f"Created user: email={email}, password={password}")

                return render(request, 'sign_up.html', {
                    'categories': Category.objects.all(),
                    'form': form,
                    'message': 'Confirmation letter were sent! Check your email please :)',
                    'type': 'success',
                })
            except smtplib.SMTPException as e:
                logging.error(f"Error happened while sending message to {email}: {str(e)}")

                return render(request, 'sign_up.html', {
                    'categories': Category.objects.all(),
                    'form': form,
                    'message': 'Something went wrong, please try again :(',
                    'type': 'error',
                })

    else:
        form = SignUpForm()

    return render(request, 'sign_up.html', {
        'categories': Category.objects.all(),
        'form': form,
    })
