from django.urls import path

from category.views import view_category

urlpatterns = [
    path('<str:category_id>/', view_category, name='category'),
]