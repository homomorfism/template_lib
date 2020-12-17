from django.contrib import admin

# Register your models here.
from post.models import Post, MyFileField


@admin.register(Post)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_publication', 'who_added', 'author', 'image_preview_small',)


@admin.register(MyFileField)
class MyFileField(admin.ModelAdmin):
    list_display = ('file',)
