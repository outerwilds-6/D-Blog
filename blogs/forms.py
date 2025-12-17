from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text'] # 不包含 date_added(自动) 和 author(后台处理)
        labels = {
            'title': '标题',
            'text': '内容',
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80}),
        }