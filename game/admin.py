# admin.py
from django.contrib import admin
from .models import Character, Chapter, Choice, Screen, HackingMiniGame, Missao, VariavelNarrativa, CenaInterativa

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    fk_name = 'screen'

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'num', 'character')
    fields = ['title', 'num', 'character']

class ScreenAdmin(admin.ModelAdmin):
    list_display = ('name', 'num', 'title','chapter')
    fields = ['name', 'num', 'title', 'content', 'custom_css', 'custom_js', 'chapter', 'hacking_mini_games', 'opcoes', 'personagens', 'mensagens_interativas', 'missoes', 'flashback', 'condicoes', 'cenas_interativas']
    inlines = [ChoiceInline]

class HackingMiniGameAdmin(admin.ModelAdmin):
    list_display = ('name', 'tipo', 'next_screen')
    fields = ['name', 'configuracao', 'descricao', 'tipo', 'next_screen']

admin.site.register(Character)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Choice)
admin.site.register(Screen, ScreenAdmin)
admin.site.register(HackingMiniGame)
admin.site.register(Missao)
admin.site.register(VariavelNarrativa)
admin.site.register(CenaInterativa)