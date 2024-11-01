from django.test import TestCase
from .models import Character, Chapter, Choice

class GameTests(TestCase):
    def setUp(self):
        self.character = Character.objects.create(name="Hero", description="The main character")
        self.chapter1 = Chapter.objects.create(title="Chapter 1", content="This is the first chapter")
        self.chapter2 = Chapter.objects.create(title="Chapter 2", content="This is the second chapter", next_chapter=self.chapter1)
        self.choice = Choice.objects.create(chapter=self.chapter1, text="Go to Chapter 2", next_chapter=self.chapter2)

    def test_chapter_content(self):
        self.assertEqual(self.chapter1.content, "This is the first chapter")

    def test_choice_text(self):
        self.assertEqual(self.choice.text, "Go to Chapter 2")