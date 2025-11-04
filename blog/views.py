from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Post, Comment


def post_detail(request, pk):
    """View for displaying a single post with its comments"""
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})


@login_required
def comment_edit(request, pk):
    """View for editing a comment - only the comment author can edit"""
    comment = get_object_or_404(Comment, pk=pk)
    
    # Check if the current user is the comment author
    if comment.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this comment.")
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            comment.content = content
            comment.save()
            messages.success(request, 'Comment updated successfully!')
            return redirect('post_detail', pk=comment.post.pk)
    
    return render(request, 'blog/comment_edit.html', {'comment': comment})


@login_required
def comment_delete(request, pk):
    """View for deleting a comment - only the comment author can delete"""
    comment = get_object_or_404(Comment, pk=pk)
    
    # Check if the current user is the comment author
    if comment.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this comment.")
    
    if request.method == 'POST':
        post_pk = comment.post.pk
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
        return redirect('post_detail', pk=post_pk)
    
    return render(request, 'blog/comment_confirm_delete.html', {'comment': comment})
