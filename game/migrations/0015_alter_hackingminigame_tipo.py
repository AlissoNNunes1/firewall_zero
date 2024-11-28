# Generated by Django 5.1.2 on 2024-11-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0014_alter_hackingminigame_tipo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hackingminigame",
            name="tipo",
            field=models.CharField(
                choices=[
                    (
                        "invasion",
                        "Hacking para invadir o sistema da célula cibernética",
                    ),
                    (
                        "pattern",
                        "Jogador resolve um puzzle para identificar padrões ocultos",
                    ),
                    (
                        "stealth",
                        "Hacking para acessar o servidor central sem ser detectado",
                    ),
                    (
                        "complex",
                        "Hacking complexo com várias etapas, refletindo a escolha do jogador",
                    ),
                    (
                        "clicker",
                        "Hacking clicker, onde o jogador enfrenta a máquina para ver quem clica mais",
                    ),
                    ("escape", "Hacking para escapar de um sistema de segurança"),
                    ("random", "Aleatório"),
                    ("defense", "Hacking para defender o ataque de python"),
                ],
                default="complex",
                max_length=50,
            ),
        ),
    ]
