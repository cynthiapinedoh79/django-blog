from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm


def post_list(request):
    """View to display list of published posts"""
    posts = Post.objects.filter(status=1)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, slug):
    """View to display a post and its comments"""
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = post.comments.filter(approved=True, parent=None)
    comment_form = CommentForm()

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            
            # Check if this is a reply to another comment
            parent_id = request.POST.get('parent_id')
            if parent_id:
                comment.parent = get_object_or_404(Comment, id=parent_id)
            
            comment.save()
            messages.success(request, 'Your comment has been submitted and is awaiting approval.')
            return redirect('post_detail', slug=slug)

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })

