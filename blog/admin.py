from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin interface for Post model"""
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin interface for Comment model with approval actions"""
    list_display = ('author', 'post', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('content', 'author__username')
    actions = ['approve_comments', 'disapprove_comments']
    
    def approve_comments(self, request, queryset):
        """Admin action to approve selected comments"""
        updated = queryset.update(approved=True)
        self.message_user(request, f'{updated} comment(s) successfully approved.')
    approve_comments.short_description = "Approve selected comments"
    
    def disapprove_comments(self, request, queryset):
        """Admin action to disapprove selected comments"""
        updated = queryset.update(approved=False)
        self.message_user(request, f'{updated} comment(s) successfully disapproved.')
    disapprove_comments.short_description = "Disapprove selected comments"
