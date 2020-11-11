from django.contrib import admin
from material.models import Material
from category.models import Category

# Register your models here.
# class MaterialTableAdmin(admin.TabularInline):
#     model = Category


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_publication', 'who_added', 'author', 'image_preview_small',)
    # inlines = [MaterialTableAdmin]
