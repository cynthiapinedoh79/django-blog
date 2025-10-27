from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Comment


@login_required
def approve_comment(request, comment_id):
    """Approve a comment"""
    comment = get_object_or_404(Comment, id=comment_id)
    comment.approved = True
    comment.save()
    messages.success(request, 'Comment approved successfully.')
    return redirect(request.META.get('HTTP_REFERER', 'admin:blog_comment_changelist'))


@login_required
def disapprove_comment(request, comment_id):
    """Disapprove a comment"""
    comment = get_object_or_404(Comment, id=comment_id)
    comment.approved = False
    comment.save()
    messages.success(request, 'Comment disapproved successfully.')
    return redirect(request.META.get('HTTP_REFERER', 'admin:blog_comment_changelist'))
