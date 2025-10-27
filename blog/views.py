from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post

# Create your views here.

def post_list(request):
    """List all posts"""
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    """Read a single post"""
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_create(request):
    """Create a new post"""
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        published = request.POST.get('published') == 'on'
        
        # Validate required fields
        if not title or not content:
            messages.error(request, 'Title and content are required.')
            return render(request, 'blog/post_form.html', {'action': 'Create'})
        
        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            published=published
        )
        messages.success(request, 'Post created successfully!')
        return redirect('post_detail', pk=post.pk)
    
    return render(request, 'blog/post_form.html', {'action': 'Create'})

@login_required
def post_update(request, pk):
    """Update an existing post"""
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        published = request.POST.get('published') == 'on'
        
        # Validate required fields
        if not title or not content:
            messages.error(request, 'Title and content are required.')
            return render(request, 'blog/post_form.html', {'post': post, 'action': 'Update'})
        
        post.title = title
        post.content = content
        post.published = published
        post.save()
        messages.success(request, 'Post updated successfully!')
        return redirect('post_detail', pk=post.pk)
    
    return render(request, 'blog/post_form.html', {'post': post, 'action': 'Update'})

@login_required
def post_delete(request, pk):
    """Delete a post"""
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('post_list')
    
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
