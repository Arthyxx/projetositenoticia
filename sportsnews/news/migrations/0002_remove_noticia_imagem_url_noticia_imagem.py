# Generated by Django 5.2 on 2025-04-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='imagem_url',
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='noticias/'),
        ),
    ]
