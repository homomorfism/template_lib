from django.urls import path

from category.views import view_category

urlpatterns = [
    path('<int:category_id>/', view_category, name='category'),
]