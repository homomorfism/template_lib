from django.contrib import admin

# Register your models here.
from post.models import Post


@admin.register(Post)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_publication', 'who_added', 'author', 'image_preview_small',)