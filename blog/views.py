from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm


def post_list(request):
    """View to display list of published posts"""
    posts = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, slug):
    """View to display a single post and its comments"""
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = post.comments.filter(approved=True).order_by('created_on')
    new_comment = None

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to comment.')
            return redirect('account_login')
        
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            messages.success(request, 'Your comment has been submitted and is awaiting approval.')
            return redirect('post_detail', slug=slug)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })
