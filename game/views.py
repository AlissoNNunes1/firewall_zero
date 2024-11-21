# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Chapter, UserProgress, Screen, HackingMiniGame, VariavelNarrativa,Choice
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

def hacking_mini_game_view(request, game_id):
    game = get_object_or_404(HackingMiniGame, id=game_id)
    configuracao = game.configuracao
    return render(request, 'game/hacking_mini_game.html', {'game': game, 'configuracao': configuracao})

def home_view(request):
    first_screen = Screen.objects.filter(num=1).first()
    if not first_screen:
        first_screen = Screen.objects.create(name="First Screen", num="1", title="First Screen", content="This is the first screen.")
    user_progress = get_user_progress(request)
    current_screen = user_progress.current_screen if user_progress.current_screen else first_screen
    return render(request, 'game/home.html', {'first_screen': first_screen, 'current_screen': current_screen})

def chapter_view(request, chapter_num):
    chapter = get_object_or_404(Chapter, num=chapter_num)
    screens = chapter.screens.all()
    user_progress = get_user_progress(request)
    
    if user_progress.current_screen and chapter.num > user_progress.current_screen.chapter.num:
        return redirect('chapter_view', chapter_num=user_progress.current_screen.chapter.num)
    
    return render(request, 'game/chapter.html', {'chapter': chapter, 'screens': screens})

def screen_view(request, screen_num):
    screen = get_object_or_404(Screen, num=screen_num)
    personagens = screen.personagens.all()
    missoes = screen.missoes.all()
    return render(request, 'game/screen.html', {'screen': screen, 'personagens': personagens, 'missoes': missoes})


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
    next_screen_num = request.POST.get('next_screen_num')
    next_screen = get_object_or_404(Screen, num=next_screen_num)
    user_progress = get_user_progress(request)
    
    # Aplicar alterações nas variáveis narrativas
    choice_id = request.POST.get('choice_id')
    if choice_id:
        choice = get_object_or_404(Choice, id=choice_id)
        if choice.variaveis_narrativas:
            for var_name, var_value in choice.variaveis_narrativas.items():
                variavel, created = VariavelNarrativa.objects.get_or_create(nome=var_name)
                variavel.valor += var_value
                variavel.save()
    
    if not user_progress.current_screen or next_screen.num > user_progress.current_screen.num:
        user_progress.current_screen = next_screen
        user_progress.save()
    
    return redirect('screen_view', screen_num=next_screen.num)

def settings(request):
    return render(request, 'game/settings.html')

def about(request):
    return render(request, 'game/about.html')

def credits(request):
    return render(request, 'game/credits.html')