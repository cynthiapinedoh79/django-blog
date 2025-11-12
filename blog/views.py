from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


class PostListView(generic.ListView):
    queryset = Post.objects.filter(status='published')
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
    def get_queryset(self):
        return Post.objects.filter(status='published')
