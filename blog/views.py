from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm


class PostListView(generic.ListView):
    """View to list all published posts"""
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6


class PostDetailView(generic.DetailView):
    """View to show a single post with comments"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(approved=True)
        context['comment_form'] = CommentForm()
        return context


def add_comment(request, slug):
    """View to add a comment to a post (requires login)"""
    post = get_object_or_404(Post, slug=slug, status=1)
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to comment.')
            return redirect('accounts:login')
        
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been posted!')
            return redirect('blog:post_detail', slug=slug)
    
    return redirect('blog:post_detail', slug=slug)

