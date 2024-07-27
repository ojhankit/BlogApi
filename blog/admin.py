# blog/admin.py

from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at', 'user']

admin.site.register(Blog, BlogAdmin)
