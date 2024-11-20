# admin.py
from django.contrib import admin
from .models import Character, Chapter, Choice, Screen



class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'num',)
    fields = ['title', 'num', 'character']
    

class ScreenChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    fk_name = 'screen'

class ScreenAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ['name', 'num','title', 'content', 'custom_css', 'custom_js', 'chapter','personagens',]
    inlines = [ScreenChoiceInline]

admin.site.register(Character)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Choice)
admin.site.register(Screen, ScreenAdmin)