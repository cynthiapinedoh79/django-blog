from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Blog post model"""
    STATUS_CHOICES = (
        (0, "Draft"),
        (1, "Published")
    )
    
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment model for blog posts"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f'Comment {self.body[:50]} by {self.name}'
