from django.urls import path
from home.views import index_view

urlpatterns = [
    path('', index_view, name='home')
]
