from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Chapter(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    next_chapter = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Choice(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    next_chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True, blank=True, related_name='previous_choices')

    def __str__(self):
        return self.text