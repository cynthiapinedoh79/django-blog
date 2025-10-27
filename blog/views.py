from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from .models import Comment


@login_required
def approve_comment(request, comment_id):
    """Approve a comment"""
    comment = get_object_or_404(Comment, id=comment_id)
    comment.approved = True
    comment.save()
    messages.success(request, 'Comment approved successfully.')
    
    # Safely handle redirect - only allow safe URLs from the same host
    referer = request.META.get('HTTP_REFERER', '')
    if referer and url_has_allowed_host_and_scheme(referer, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
        return redirect(referer)
    return redirect(reverse('admin:blog_comment_changelist'))


@login_required
def disapprove_comment(request, comment_id):
    """Disapprove a comment"""
    comment = get_object_or_404(Comment, id=comment_id)
    comment.approved = False
    comment.save()
    messages.success(request, 'Comment disapproved successfully.')
    
    # Safely handle redirect - only allow safe URLs from the same host
    referer = request.META.get('HTTP_REFERER', '')
    if referer and url_has_allowed_host_and_scheme(referer, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
        return redirect(referer)
    return redirect(reverse('admin:blog_comment_changelist'))
