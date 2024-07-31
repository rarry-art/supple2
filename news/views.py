from django.shortcuts import render, get_object_or_404
from .models import Story, Comment

def story_list(request):
    stories = Story.objects.order_by('-points')
    return render(request, 'news/story_list.html', {'stories': stories})

def story_detail(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    return render(request, 'news/story_detail.html', {'story': story})