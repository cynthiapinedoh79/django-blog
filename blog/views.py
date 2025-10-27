from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    """View for displaying a list of published blog posts"""
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'
    paginate_by = 6


class PostDetail(generic.DetailView):
    """View for displaying a single blog post"""
    model = Post
    template_name = 'blog/post_detail.html'

    def get_queryset(self):
        """Only show published posts"""
        return Post.objects.filter(status=1)

