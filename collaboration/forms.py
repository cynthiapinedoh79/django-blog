from django import forms
from .models import CollaborationRequest


class CollaborationForm(forms.ModelForm):
    """Form for collaboration requests with validation."""
    
    class Meta:
        model = CollaborationRequest
        fields = ['name', 'email', 'website', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://yourwebsite.com (Optional)'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about your collaboration proposal...',
                'rows': 5
            }),
        }
        labels = {
            'name': 'Name *',
            'email': 'Email *',
            'website': 'Website/Portfolio URL',
            'message': 'Message/Proposal *',
        }
    
    def clean_email(self):
        """Validate email format."""
        email = self.cleaned_data.get('email')
        if email:
            # Django's EmailField already validates format, but we can add custom validation
            return email.lower()
        return email
