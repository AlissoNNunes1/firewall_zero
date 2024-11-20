from django.test import TestCase
from .models import Character, Chapter, Choice, Screen

class GameTests(TestCase):
    def setUp(self):
        self.character = Character.objects.create(name="Hero", description="The main character")
        self.chapter1 = Chapter.objects.create(title="Chapter 1", content="This is the first chapter", character=self.character)
        self.chapter2 = Chapter.objects.create(title="Chapter 2", content="This is the second chapter", next_chapter=self.chapter1, character=self.character)
        self.screen = Screen.objects.create(title="Screen 1", content="This is a custom screen")
        self.choice1 = Choice.objects.create(chapter=self.chapter1, text="Go to Chapter 2", next_chapter=self.chapter2)
        self.choice2 = Choice.objects.create(chapter=self.chapter1, text="Go to Screen 1", next_screen=self.screen)

    def test_chapter_content(self):
        self.assertEqual(self.chapter1.content, "This is the first chapter")

    def test_choice_text(self):
        self.assertEqual(self.choice1.text, "Go to Chapter 2")
        self.assertEqual(self.choice2.text, "Go to Screen 1")