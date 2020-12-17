import os

from django.contrib.auth.decorators import login_required
from django.http.response import FileResponse, Http404
from django.conf import settings
# Create your views here.
from post.models import FileField


# In the future add functionality that user can not download attachments from hidden posts
# TODO change Http404 to custom template with error message

@login_required(redirect_field_name='login')
def file_download(request, file_id):
    try:
        file_path = FileField.objects.get(pk=file_id)
        if settings.DEBUG:
            print("DEBUG: path to file=", file_path)
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    except Exception:
        raise Http404("File does not exist")
