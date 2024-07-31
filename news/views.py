from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Story, Comment
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

def story_list(request):
    stories = Story.objects.order_by('-points')
    return render(request, 'news/story_list.html', {'stories': stories})

def story_detail(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    return render(request, 'news/story_detail.html', {'story': story})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('story_list')
    else:
        form = SignUpForm()
    return render(request, 'news/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('story_list')
    else:
        form = AuthenticationForm()
    return render(request, 'news/login.html', {'form': form})

@login_required
def submit_story(request):
    # 스토리 제출 로직 (아직 구현되지 않음)
    pass