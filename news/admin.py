from django.contrib import admin
from .models import Story, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'points', 'user', 'created_at')
    list_filter = ('created_at', 'points')
    search_fields = ('title', 'url', 'user__username')
    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('story', 'user', 'text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('text', 'user__username', 'story__title')
