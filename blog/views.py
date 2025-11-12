from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """View for listing all published blog posts."""
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6


class PostDetail(generic.DetailView):
    """View for displaying a single blog post detail."""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        """Only allow published posts to be viewed."""
        return Post.objects.filter(status=1)
