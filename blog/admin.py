from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('content', 'author__username')
    actions = ['approve_comments', 'disapprove_comments']

    def approve_comments(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, f'{updated} comment(s) successfully approved.')
    approve_comments.short_description = 'Approve selected comments'

    def disapprove_comments(self, request, queryset):
        updated = queryset.update(approved=False)
        self.message_user(request, f'{updated} comment(s) successfully disapproved.')
    disapprove_comments.short_description = 'Disapprove selected comments'
