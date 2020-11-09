from django.urls import path
from static.home.views import index_view

urlpatterns = [
    path('', index_view, name='home')
]
