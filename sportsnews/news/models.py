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
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class ConteudoNoticia(models.Model):
    TIPO_CHOICES = [
        ('texto', 'Texto'),
        ('imagem', 'Imagem'),
        ('video', 'Vídeo'),
    ]

    noticia = models.ForeignKey(Noticia, related_name='conteudos', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    texto = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='conteudos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    ordem = models.PositiveIntegerField(default=0)  # para ordenar os blocos

    def __str__(self):
        return f"{self.tipo} - {self.noticia.titulo}"
