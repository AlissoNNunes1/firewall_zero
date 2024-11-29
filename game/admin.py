# admin.py
from django.contrib import admin
from .models import Character, Chapter, Choice, Screen, HackingMiniGame, Missao, VariavelNarrativa, CenaInterativa
from .forms import HackingMiniGameForm

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    fk_name = 'screen'

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'num', 'character')
    fields = ['title', 'num', 'character', 'trilha_sonora']  # Adicione 'trilha_sonora' aos campos

class ScreenAdmin(admin.ModelAdmin):
    list_display = ('name', 'num', 'title','chapter')
    fields = ['name', 'num', 'title', 'content', 'custom_css', 'custom_js', 'chapter',  'opcoes', 'personagens', 'mensagens_interativas', 'missoes', 'flashback', 'condicoes', 'cenas_interativas']
    inlines = [ChoiceInline]

class HackingMiniGameAdmin(admin.ModelAdmin):
    form = HackingMiniGameForm
    list_display = ('name', 'tipo', 'next_screen')
    fields = ['name', 'descricao', 'tipo', 'next_screen', 'dificuldade', 'tempo_limite']

admin.site.register(Character)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Choice)
admin.site.register(Screen, ScreenAdmin)
admin.site.register(HackingMiniGame, HackingMiniGameAdmin)
admin.site.register(Missao)
admin.site.register(VariavelNarrativa)
admin.site.register(CenaInterativa)