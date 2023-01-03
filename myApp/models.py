from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name

class Product(models.Model):
    image=models.ImageField(null=True, blank=True, upload_to='my_imgs')
    name=models.CharField(max_length=255)
    description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    availability=models.CharField(max_length=70)
    date=models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()

    def __str__(self):
        return self.name + ' | ' + 'Rs ' + str(self.price)
    