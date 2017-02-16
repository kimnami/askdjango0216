from django import forms
from .models import Webtoon

class PostForm(forms.ModelForm):
    class Meta:
        model = Webtoon
        fields = ['title']