# admin.py
from django.contrib import admin
from .models import Character, Chapter, Choice, Screen, HackingMiniGame,  Missao, VariavelNarrativa, CenaInterativa, Missao



class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'num',)
    fields = ['title', 'num', 'character']
    

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    fk_name = 'screen'
    fields = ['text', 'next_screen', 'hacking_mini_game', 'variaveis_narrativas']

class ScreenAdmin(admin.ModelAdmin):
    list_display = ('name', 'num', 'title')
    fields = ['name', 'num', 'title', 'content', 'custom_css', 'custom_js', 'chapter', 'hacking_mini_games', 'opcoes', 'personagens', 'mensagens_interativas', 'missoes', 'flashback', 'condicoes', 'cenas_interativas']
    inlines = [ChoiceInline]

admin.site.register(Character)
admin.site.register(Chapter)
admin.site.register(Choice)
admin.site.register(Screen, ScreenAdmin)
admin.site.register(HackingMiniGame)
admin.site.register(Missao)
admin.site.register(VariavelNarrativa)
admin.site.register(CenaInterativa)