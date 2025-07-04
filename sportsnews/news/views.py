from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory

from .models import Noticia, ConteudoNoticia
from .forms import NoticiaForm, ConteudoNoticiaForm

# InlineFormSet -> Gerenciar dinamicamente
ConteudoFormSet = inlineformset_factory(
    Noticia,
    ConteudoNoticia,
    form=ConteudoNoticiaForm,
    extra=1,
    can_delete=True
)

def home(request):
    destaques = Noticia.objects.filter(destaque=True).order_by('-data_publicacao')
    noticias = Noticia.objects.all()
    categorias = Noticia.categoria_choices
    return render(request, 'home.html', {
        'destaques': destaques,
        'noticias': noticias,
        'categorias': categorias
    })

def categoria(request, categoria):
    noticias = Noticia.objects.filter(categoria=categoria).order_by('-data_publicacao')
    return render(request, 'categoria.html', {'noticias': noticias, 'categoria': categoria})

def noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    conteudos = noticia.conteudos.order_by('ordem')
    return render(request, 'noticia.html', {'noticia': noticia, 'conteudos': conteudos})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'login.html')

@login_required(login_url='/login')
def admin_dashboard(request):
    noticias = Noticia.objects.all()
    return render(request, 'admin_dashboard.html', {'noticias': noticias})

@login_required(login_url='/login')
def destacar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    noticia.destaque = True
    noticia.save()
    return redirect('admin_dashboard')

@login_required(login_url='/login')
def remover_destaque(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    noticia.destaque = False
    noticia.save()
    return redirect('admin_dashboard')

@login_required(login_url='/login')
def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)

    ConteudoFormSet = inlineformset_factory(
        Noticia,
        ConteudoNoticia,
        form=ConteudoNoticiaForm,
        extra=1,
        can_delete=True
    )

    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        formset = ConteudoFormSet(request.POST, request.FILES, instance=noticia, prefix='conteudo')

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('admin_dashboard')
    else:
        form = NoticiaForm(instance=noticia)
        formset = ConteudoFormSet(instance=noticia, prefix='conteudo')

    return render(request, 'editar_noticia.html', {'form': form, 'formset': formset})

@login_required(login_url='/login')
def add_noticia(request):
    ConteudoFormSet = inlineformset_factory(
        Noticia,
        ConteudoNoticia,
        form=ConteudoNoticiaForm,
        extra=1,
        can_delete=True
    )

    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        formset = ConteudoFormSet(request.POST, request.FILES, prefix='conteudo')

        if form.is_valid() and formset.is_valid():
            noticia = form.save()
            formset.instance = noticia
            formset.save()
            return redirect('admin_dashboard')
    else:
        form = NoticiaForm()
        formset = ConteudoFormSet(prefix='conteudo')

    return render(request, 'add_noticia.html', {
        'form': form,
        'formset': formset
    })

@login_required(login_url='/login')
def excluir_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('admin_dashboard')
    return render(request, 'excluir_noticia.html', {'noticia': noticia})
