from django.contrib import admin
from category.models import Category
from material.models import Material


# Register your models here.
# class CategoryTableAdmin(admin.TabularInline):
#     model = Material.categories.through


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('text',)
    # inlines = [CategoryTableAdmin,]
