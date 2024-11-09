# Generated by Django 5.1.2 on 2024-11-09 00:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_chapter_character_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='character_image',
        ),
        migrations.AddField(
            model_name='chapter',
            name='character',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='game.character'),
            preserve_default=False,
        ),
    ]