from django import forms
from .models import Postimg

class PostForm(forms.ModelForm):
    class Meta:
        model = Postimg
        fields = ['title', 'description', 'image']