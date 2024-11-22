# forms.py
from django import forms
from .models import Chapter, HackingMiniGame

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'num', 'character']
        

class HackingMiniGameForm(forms.ModelForm):
    DIFICULDADE_CHOICES = [
        ('fácil', 'Fácil'),
        ('média', 'Média'),
        ('difícil', 'Difícil'),
    ]

    dificuldade = forms.ChoiceField(choices=DIFICULDADE_CHOICES, label='Dificuldade')
    tempo_limite = forms.IntegerField(label='Tempo Limite (segundos)', min_value=10, max_value=300)

    class Meta:
        model = HackingMiniGame
        fields = ['name', 'descricao', 'tipo', 'next_screen', 'dificuldade', 'tempo_limite']

    def clean(self):
        cleaned_data = super().clean()
        configuracao = {
            'dificuldade': cleaned_data.get('dificuldade'),
            'tempo_limite': cleaned_data.get('tempo_limite'),
        }
        self.instance.configuracao = configuracao
        return cleaned_data