from django.contrib import admin
from material.models import Material
# Register your models here.

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass


