from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


# models.py
class HackingMiniGame(models.Model):
    HACKING_TYPES = [
        ('invasion', 'Hacking para invadir o sistema da célula cibernética'),
        ('pattern', 'Jogador resolve um puzzle para identificar padrões ocultos'),
        ('stealth', 'Hacking para acessar o servidor central sem ser detectado'),
        ('complex', 'Hacking complexo com várias etapas, refletindo a escolha do jogador'),
        ('clicker', 'Hacking clicker, onde o jogador enfrenta a máquina para ver quem clica mais'),
        ('escape', 'Hacking para escapar de um sistema de segurança'),
        ('random', 'Aleatório'),  
        ('defense','Hacking para defender o ataque de python'), 
        ('cerco', 'Hacking para cercar o python'),
        ('furtivo', 'infiltração em um sistema protegido sem ser detectado pelas câmeras de segurança, coletando dados críticos e evitando armadilhas'),
        ('final','Minigame final contra o Python'),
        
        
    ]

    name = models.CharField(max_length=100)
    configuracao = models.JSONField()
    descricao = models.TextField()
    dificuldade = models.CharField(max_length=50, default="média")
    tempo_limite = models.IntegerField(default=30)
    tipo = models.CharField(max_length=50, choices=HACKING_TYPES, default="complex")
    next_screen = models.ForeignKey('Screen', on_delete=models.SET_NULL, null=True, blank=True, related_name='previous_mini_games')

    def __str__(self):
        return self.name


class Missao(models.Model):
    TIPOS_MISSAO = [
        ('furtividade', 'Furtividade'),
        ('combate', 'Combate'),
    ]

    descricao = models.TextField()
    tipo = models.CharField(max_length=50, choices=TIPOS_MISSAO)
    parametros = models.JSONField()

    def __str__(self):
        return self.descricao


class VariavelNarrativa(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    reputation = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', default='images/zero.png')

    def __str__(self):
        return self.name

    def get_reputation(self):
        return self.reputation


class Chapter(models.Model):
    title = models.CharField(max_length=100)
    num = models.IntegerField()
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    trilha_sonora = models.FileField(upload_to='trilhas_sonoras/', blank=True, null=True)  # Novo campo de trilha sonora

    def __str__(self):
        return self.title

class Screen(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    custom_css = models.TextField(blank=True, null=True)
    custom_js = models.TextField(blank=True, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='screens')
    
    opcoes = models.JSONField(blank=True, null=True)
    personagens = models.ManyToManyField(Character, blank=True)
    mensagens_interativas = models.TextField(blank=True, null=True)
    missoes = models.ManyToManyField(Missao, blank=True)
    flashback = models.BooleanField(default=False)
    condicoes = models.JSONField(blank=True, null=True)
    cenas_interativas = models.ManyToManyField(
        'CenaInterativa', 
        blank=True, 
        related_name='linked_screens'  # Alterado para evitar conflito
    )
    alinhamento = models.CharField(max_length=50, blank=True, null=True)  # Novo campo para alinhamento

    def __str__(self):
        return self.title


class Choice(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='choices', null=True, blank=True)
    text = models.CharField(max_length=200)
    next_screen = models.ForeignKey(Screen, on_delete=models.SET_NULL, null=True, blank=True, related_name='previous_choices')
    hacking_mini_game = models.ForeignKey(HackingMiniGame, on_delete=models.SET_NULL, null=True, blank=True, related_name='choices')
    variaveis_narrativas = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.text


class CenaInterativa(models.Model):
    nome = models.CharField(max_length=100)
    configuracao = models.JSONField()
    descricao = models.TextField()
    mini_jogos = models.ManyToManyField(HackingMiniGame, blank=True)
    escolhas = models.ManyToManyField(Choice, blank=True, related_name='cenas_interativas')
    screens = models.ManyToManyField(
        Screen, 
        blank=True, 
        related_name='cenas_interativas_instances'  # Alterado para evitar conflito
    )

    def __str__(self):
        return self.nome



class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    current_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username if self.user else self.session_key} - {self.current_url}"
