from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_published')
    list_filter = ('created_at', 'last_updated_at', 'publisher')
    search_fields = ('publisher', 'title', 'content')
