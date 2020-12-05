from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import render

# Create your views here.
from post.models import Post


@login_required(redirect_field_name='login')
def post_page(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)



    except:
        raise Http404("File not found!")