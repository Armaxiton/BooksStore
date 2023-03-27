from django import forms 

from .models import *

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ['title', 'author', 'price', 'year', 'slug', 'genre']