# views.py
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Chapter, UserProgress, Screen, HackingMiniGame, VariavelNarrativa, Choice, Character
from .forms import ChapterForm
from django.http import JsonResponse
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

# views.py
def hacking_mini_game_view(request, game_id):
    game = get_object_or_404(HackingMiniGame, id=game_id)
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('completed'):
            if game.next_screen:
                return JsonResponse({'next_screen_url': reverse('screen_view', args=[game.next_screen.chapter.num, game.next_screen.num])})
            else:
                return JsonResponse({'message': 'Mini-jogo concluído, mas nenhuma próxima tela configurada.'})
        else:
            return JsonResponse({'lose_url': reverse('lose')})
    
    # Selecionar o template correto com base no tipo de mini-jogo
    template_name = ''
    if game.tipo == 'invasion':
        template_name = 'game/hacking_mini_game_invasion.html'
    elif game.tipo == 'pattern':
        template_name = 'game/hacking_mini_game_pattern.html'
    elif game.tipo == 'stealth':
        template_name = 'game/hacking_mini_game_stealth.html'
    elif game.tipo == 'complex':
        template_name = 'game/hacking_mini_game_complex.html'
    elif game.tipo == 'clicker':
        template_name = 'game/hacking_mini_game_clicker.html'
    
    return render(request, template_name, {'game': game, 'configuracao': game.configuracao})

def home_view(request):
    # Carregar dados essenciais do banco de dados
    first_screen = Screen.objects.filter(num=1).first()
    if not first_screen:
        first_chapter = Chapter.objects.first()
        if not first_chapter:
            first_chapter = Chapter.objects.create(title="First Chapter", num=1, character=Character.objects.first())
        first_screen = Screen.objects.create(name="First Screen", num=1, title="First Screen", content="This is the first screen.", chapter=first_chapter)
    
    user_progress = get_user_progress(request)
    current_screen = user_progress.current_screen if user_progress.current_screen else first_screen
    
    # Carregar outros dados essenciais, se necessário
    characters = Character.objects.all()
    chapters = Chapter.objects.all()
    screens = Screen.objects.all()
    
    return render(request, 'game/home.html', {
        'first_screen': first_screen,
        'current_screen': current_screen,
        'characters': characters,
        'chapters': chapters,
        'screens': screens,
    })

def chapter_view(request, chapter_num):
    chapter = get_object_or_404(Chapter, num=chapter_num)
    screens = chapter.screens.all()
    user_progress = get_user_progress(request)
    
    if user_progress.current_screen and chapter.num > user_progress.current_screen.chapter.num:
        return redirect('chapter_view', chapter_num=user_progress.current_screen.chapter.num)
    
    return render(request, 'game/chapter.html', {'chapter': chapter, 'screens': screens})

def screen_view(request, chapter_num, screen_num):
    screen = get_object_or_404(Screen, chapter__num=chapter_num, num=screen_num)
    personagens = screen.personagens.all()
    missoes = screen.missoes.all()
    cenas_interativas = screen.cenas_interativas.all()

    # Verificar o alinhamento do jogador
    alinhamento = None
    if screen.alinhamento:
        alinhamento = screen.alinhamento

    return render(request, 'game/screen.html', {
        'screen': screen,
        'personagens': personagens,
        'missoes': missoes,
        'cenas_interativas': cenas_interativas,
        'alinhamento': alinhamento,
    })
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
    
    # Determinar o alinhamento do jogador
    alinhamento = determine_alignment(user_progress)
    if not user_progress.current_screen or next_screen.num > user_progress.current_screen.num:
        user_progress.current_screen = next_screen
        user_progress.save()
    
    return redirect('screen_view', chapter_num=next_screen.chapter.num, screen_num=next_screen.num)

def determine_alignment(user_progress):
    # Lógica para determinar o alinhamento com base nas variáveis narrativas
    variaveis = VariavelNarrativa.objects.all()
    alinhamento = "Neutro"
    if variaveis.filter(nome="bondade").exists() and variaveis.get(nome="bondade").valor > 10:
        alinhamento = "Bondoso"
    elif variaveis.filter(nome="maldade").exists() and variaveis.get(nome="maldade").valor > 10:
        alinhamento = "Maligno"
    return alinhamento

def settings(request):
    return render(request, 'game/settings.html')

def about(request):
    return render(request, 'game/about.html')

def credits(request):
    return render(request, 'game/credits.html')

def lose(request):
    return render(request, 'game/lose.html')