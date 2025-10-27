from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """Model representing a blog post"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=((0, 'Draft'), (1, 'Published')), default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
