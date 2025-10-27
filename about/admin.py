from django.contrib import admin
from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    Admin interface for About model.
    """
    list_display = ('title', 'updated_on')
    search_fields = ['title', 'content']
