from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'content')
    actions = ['approve_comments', 'disapprove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f'{queryset.count()} comments have been approved.')
    approve_comments.short_description = 'Approve selected comments'

    def disapprove_comments(self, request, queryset):
        queryset.update(approved=False)
        self.message_user(request, f'{queryset.count()} comments have been disapproved.')
    disapprove_comments.short_description = 'Disapprove selected comments'
