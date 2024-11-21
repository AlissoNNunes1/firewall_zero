# Generated by Django 5.1.2 on 2024-11-21 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_choice_variaveis_narrativas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screen',
            name='cenas_interativas',
        ),
        migrations.AddField(
            model_name='cenainterativa',
            name='escolhas',
            field=models.ManyToManyField(blank=True, to='game.choice'),
        ),
        migrations.AddField(
            model_name='cenainterativa',
            name='mini_jogos',
            field=models.ManyToManyField(blank=True, to='game.hackingminigame'),
        ),
        migrations.AddField(
            model_name='cenainterativa',
            name='screens',
            field=models.ManyToManyField(blank=True, to='game.screen'),
        ),
    ]
