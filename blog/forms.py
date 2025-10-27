from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Form for users to submit comments"""
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment here...'
            }),
        }
        labels = {
            'content': 'Comment',
        }
