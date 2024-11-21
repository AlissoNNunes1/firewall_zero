# models.py
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.postgres.fields import JSONField

class HackingMiniGame(models.Model):
    name = models.CharField(max_length=100)
    configuracao = models.JSONField()
    descricao = models.TextField()

    def __str__(self):
        return self.name
class CenaInterativa(models.Model):
    nome = models.CharField(max_length=100)
    configuracao = models.JSONField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome
class Missao(models.Model):
    descricao = models.TextField()
    tipo = models.CharField(max_length=50, choices=[('furtividade', 'Furtividade'), ('combate', 'Combate')])
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
    image = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.name

    def get_reputation(self):
        return self.reputation

class Chapter(models.Model):
    title = models.CharField(max_length=100)
    num = models.IntegerField(default=0)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='chapters')

    def __str__(self):
        return self.title

# models.py
class Screen(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    custom_css = models.TextField(blank=True, null=True)
    custom_js = models.TextField(blank=True, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='screens')
    hacking_mini_games = models.ManyToManyField(HackingMiniGame, blank=True)
    opcoes = models.JSONField(blank=True, null=True)
    personagens = models.ManyToManyField(Character, blank=True)
    mensagens_interativas = models.TextField(blank=True, null=True)
    missoes = models.ManyToManyField(Missao, blank=True)
    flashback = models.BooleanField(default=False)
    condicoes = models.JSONField(blank=True, null=True)
    cenas_interativas = models.ManyToManyField(CenaInterativa, blank=True)
    def __str__(self):
        return self.title

class Choice(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='choices', null=True, blank=True)
    text = models.CharField(max_length=200)
    next_screen = models.ForeignKey(Screen, on_delete=models.SET_NULL, null=True, blank=True, related_name='previous_choices')
    hacking_mini_game = models.ForeignKey(HackingMiniGame, on_delete=models.SET_NULL, null=True, blank=True, related_name='choices')
    def __str__(self):
        return self.text

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    session = models.OneToOneField(Session, on_delete=models.CASCADE, null=True, blank=True)
    current_screen = models.ForeignKey(Screen, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.user:
            return f"{self.user.username}'s progress"
        return f"Session {self.session.session_key}'s progress"