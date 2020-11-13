from django.urls import path, re_path

from post.views import post_page

urlpatterns = [
    path('<int:post_id>/', post_page, name = 'post-detail'),
]