from django import forms
from app.models import Category

class CategoryFrom(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        