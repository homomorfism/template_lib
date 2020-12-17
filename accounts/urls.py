from django.urls import path

from accounts.views import change_password_view, reset_password_view, login_view, logout_view, sign_up_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('change_password/', change_password_view, name='change_password'),
    path('reset_password/', reset_password_view, name='reset_password'),
    path('sign_up/', sign_up_view, name='sign_up'),
]
