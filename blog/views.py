from django.shortcuts import render, get_object_or_404
from .models import Post


def post_detail(request, slug):
    """
    Display an individual post with its comments.
    Users can click on a post to read the conversation (AC2).
    """
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = post.comments.filter(approved=True).order_by('created_on')
    
    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
            'comments': comments,
        }
    )
