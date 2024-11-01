from django.shortcuts import render, get_object_or_404
from .models import Chapter
from .forms import ChapterForm

def chapter_view(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    return render(request, 'game/chapter.html', {'chapter': chapter})

def home_view(request):
    first_chapter = Chapter.objects.first()
    return render(request, 'game/home.html', {'first_chapter': first_chapter})

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