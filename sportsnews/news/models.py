from django.db import models

class Noticia(models.Model):
    categoria_choices = [
        ('futebol', 'Futebol'),
        ('basquete', 'Basquete'),
        ('baseball', 'Baseball'),
        ('hockey', 'Hockey'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.CharField(max_length=20, choices=categoria_choices)
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)  # Usando ImageField
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
