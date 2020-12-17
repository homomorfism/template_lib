from django.contrib.auth.decorators import login_required


# Create your views here.

# TODO add templates for login and implement login_view
def login_view(request):
    pass


# TODO implement logout_view
@login_required(redirect_field_name='login')
def logout_view(request):
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