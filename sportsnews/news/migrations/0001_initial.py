# Generated by Django 5.2 on 2025-04-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(choices=[('futebol', 'Futebol'), ('basquete', 'Basquete'), ('baseball', 'Baseball'), ('hockey', 'Hockey')], max_length=20)),
                ('imagem_url', models.URLField()),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
