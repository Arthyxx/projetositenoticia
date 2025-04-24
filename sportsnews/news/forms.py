from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'descricao', 'categoria', 'imagem']

    imagem = forms.ImageField(required=False)
