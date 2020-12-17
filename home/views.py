from django.shortcuts import render


# Create your views here.

# TODO add search engine which will display recently added material
from category.models import Category
from post.models import Post


def index_view(request):

    context = {
        "posts": Post.objects.filter(visibility='1').all()[:20],
        "categories": Category.objects.all(),
    }

    return render(request, "index.html", context)
