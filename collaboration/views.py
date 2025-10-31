from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import logging
from .forms import CollaborationForm

logger = logging.getLogger(__name__)

# Create your views here.

def collaboration_request(request):
    """Handle collaboration form submission."""
    if request.method == 'POST':
        form = CollaborationForm(request.POST)
        if form.is_valid():
            # Save the collaboration request
            collaboration = form.save()
            
            # Send email notification to site owner (AC4)
            subject = f"New Collaboration Request from {collaboration.name}"
            message = f"""
New collaboration request received:

Name: {collaboration.name}
Email: {collaboration.email}
Website: {collaboration.website or 'Not provided'}

Message:
{collaboration.message}

Submitted at: {collaboration.created_at}
"""
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                # Log error but don't fail the submission
                logger.error(f"Error sending email: {e}")
            
            # Display success message (AC2)
            messages.success(
                request, 
                'Thank you for your collaboration request! Your proposal has been sent successfully. '
                'We will review it and get back to you soon.'
            )
            return redirect('collaboration:request')
        else:
            # Display error message for invalid form (AC3)
            messages.error(
                request,
                'Please correct the errors below and try again.'
            )
    else:
        form = CollaborationForm()
    
    return render(request, 'collaboration/request_form.html', {'form': form})

