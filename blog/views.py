from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """View to display list of published posts"""
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'
    paginate_by = 6


class PostDetail(generic.DetailView):
    """View to display post detail with comments"""
    model = Post
    template_name = 'blog/post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get approved comments for this post
        context['comments'] = self.object.comments.filter(approved=True).order_by('created_on')
        context['comment_count'] = context['comments'].count()
        return context
