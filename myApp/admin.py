from django.contrib import admin
from .models import Product, Category

# Register your models here.
@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'name', 'description', 'price', 'availability', 'date', 'category')

@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name']