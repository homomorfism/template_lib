from django import forms
from post.models import Post

class UploadForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author', 'short_summary', 'description', 'image_preview_small', 'image_preview_big', '')
