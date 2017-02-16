from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']

    def clean_content(self):
        content = self.cleaned_data_get('content','')
        if len(content) % 2 == 0 :
            self.add_error('content','홀수 길이로 입력하세요.')
        return content

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
