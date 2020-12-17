from django.contrib.auth.decorators import login_required
from django.http.response import Http404

# Create your views here.
from post.models import Post


# TODO 404 -> page does not exists
@login_required(redirect_field_name='login')
def post_page(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)



    except:
        raise Http404("File not found!")
