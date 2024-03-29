from django import forms
from . models import Comments, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image',
                  'excerpt', 'status', 'category')
