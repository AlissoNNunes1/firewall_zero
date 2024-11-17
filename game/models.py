from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

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
    content = models.TextField()
    next_chapter = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='chapters')

    def __str__(self):
        return self.title

class Choice(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    next_chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True, blank=True, related_name='previous_choices')

    def __str__(self):
        return self.text

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    session = models.OneToOneField(Session, on_delete=models.CASCADE, null=True, blank=True)
    current_chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.user:
            return f"{self.user.username}'s progress"
        return f"Session {self.session.session_key}'s progress"