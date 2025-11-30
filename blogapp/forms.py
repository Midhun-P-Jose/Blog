from django import forms
from .models import blogmodel
class blogform(forms.ModelForm):
    
    class Meta:
        model = blogmodel
        fields = ['Title','Body']
        