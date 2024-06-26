# Generated by Django 5.0.3 on 2024-03-26 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='juego',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='juegos/static/img'),
        ),
        migrations.AlterField(
            model_name='juego',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.categoria'),
        ),
    ]
