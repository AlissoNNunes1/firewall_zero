from django.contrib import admin
from .models import Character, Chapter, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    fk_name = 'chapter'  # Especifica qual ForeignKey usar

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'next_chapter')
    inlines = [ChoiceInline]

admin.site.register(Character)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Choice)