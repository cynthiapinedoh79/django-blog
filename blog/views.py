from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Post, Comment
from .forms import CommentForm


def post_list(request):
    """Display list of published posts"""
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """Display post detail with comments"""
    post = get_object_or_404(Post, pk=pk, published=True)
    comments = post.comments.all()
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                messages.success(request, 'Comment added successfully!')
                return redirect('post_detail', pk=pk)
        else:
            messages.error(request, 'You must be logged in to comment.')
            return redirect('login')
    else:
        form = CommentForm()
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


@login_required
def comment_edit(request, pk):
    """Edit a comment - only by the author"""
    comment = get_object_or_404(Comment, pk=pk)
    
    # Check if user is the comment author
    if comment.author != request.user:
        return HttpResponseForbidden("You can only edit your own comments.")
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully!')
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'blog/comment_edit.html', {
        'form': form,
        'comment': comment
    })


@login_required
def comment_delete(request, pk):
    """Delete a comment - only by the author"""
    comment = get_object_or_404(Comment, pk=pk)
    
    # Check if user is the comment author
    if comment.author != request.user:
        return HttpResponseForbidden("You can only delete your own comments.")
    
    post_pk = comment.post.pk
    
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
        return redirect('post_detail', pk=post_pk)
    
    return render(request, 'blog/comment_confirm_delete.html', {
        'comment': comment
    })
