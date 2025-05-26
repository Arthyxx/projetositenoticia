from django import forms
from .models import Noticia, ConteudoNoticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'descricao', 'categoria', 'imagem']

class ConteudoNoticiaForm(forms.ModelForm):
    class Meta:
        model = ConteudoNoticia
        fields = ['tipo', 'texto', 'imagem', 'video_url', 'ordem']
