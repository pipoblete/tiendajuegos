# Generated by Django 5.0.3 on 2024-03-30 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0004_remove_juego_id_juego_juego_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='precio',
            field=models.IntegerField(),
        ),
    ]