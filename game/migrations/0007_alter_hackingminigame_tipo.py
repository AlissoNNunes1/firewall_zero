# Generated by Django 5.1.2 on 2024-11-22 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_hackingminigame_next_screen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackingminigame',
            name='tipo',
            field=models.CharField(choices=[('invasion', 'Hacking para invadir o sistema da célula cibernética'), ('pattern', 'Jogador resolve um puzzle para identificar padrões ocultos'), ('stealth', 'Hacking para acessar o servidor central sem ser detectado'), ('complex', 'Hacking complexo com várias etapas, refletindo a escolha do jogador')], default='complex', max_length=50),
        ),
    ]