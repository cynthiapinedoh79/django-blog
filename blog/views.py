from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """View to display paginated list of posts"""
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'
    paginate_by = 6
