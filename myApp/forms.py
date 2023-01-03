from django import forms
from .models import Product

class productRegistration(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'id','image', 'name', 'description', 'price', 'availability','category']

        widgets = {
            'image' : forms.FileInput(attrs={'class':'form-control form-control-sm', 'width':"300", 'height':"300"}),
            'name' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Mention the product name'}),
            'description' : forms.Textarea(attrs={'class':'form-control form-control-sm', 'placeholder':'Mention product details'}),
            'price' : forms.NumberInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Mention the price'}),
            'availability' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Mention if the product is available or not'}),
            'category' : forms.Select(attrs={'class':'form-control form-control-sm'}),
        }