from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Form for creating and replying to comments"""
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter your comment...'
            })
        }
        labels = {
            'content': 'Comment'
        }
