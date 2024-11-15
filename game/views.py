from django.shortcuts import render, get_object_or_404, redirect
from .models import Chapter, UserProgress
from .forms import ChapterForm
from django.views.decorators.http import require_POST
from django.contrib.sessions.models import Session

def get_user_progress(request):
    if request.user.is_authenticated:
        user_progress, created = UserProgress.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        session = Session.objects.get(session_key=session_key)
        user_progress, created = UserProgress.objects.get_or_create(session=session)
    return user_progress

def chapter_view(request, chapter_num):
    chapter = get_object_or_404(Chapter, num=chapter_num)
    user_progress = get_user_progress(request)
    
    if user_progress.current_chapter and chapter.num > user_progress.current_chapter.num:
        return redirect('chapter_view', chapter_num=user_progress.current_chapter.num)
    
    return render(request, 'game/chapter.html', {'chapter': chapter})

def home_view(request):
    first_chapter = Chapter.objects.first()
    user_progress = get_user_progress(request)
    current_chapter = user_progress.current_chapter if user_progress.current_chapter else first_chapter
    return render(request, 'game/home.html', {'first_chapter': first_chapter, 'current_chapter': current_chapter})

def chapter_list(request):
    chapters = Chapter.objects.all()
    return render(request, 'game/chapter_list.html', {'chapters': chapters})

def add_chapter(request):
    if request.method == "POST":
        form = ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chapter_list')
    else:
        form = ChapterForm()
    return render(request, 'game/add_chapter.html', {'form': form})

@require_POST
def update_progress(request):
    next_chapter_num = request.POST.get('next_chapter_num')
    next_chapter = get_object_or_404(Chapter, num=next_chapter_num)
    user_progress = get_user_progress(request)
    
    if not user_progress.current_chapter or next_chapter.num > user_progress.current_chapter.num:
        user_progress.current_chapter = next_chapter
        user_progress.save()
    
    return redirect('chapter_view', chapter_num=next_chapter_num)

def settings(request):
    return render(request, 'game/settings.html')

def about(request):
    return render(request, 'game/about.html')

def credits(request):
    return render(request, 'game/credits.html')