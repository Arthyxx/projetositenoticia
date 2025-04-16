from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Noticia
from .forms import NoticiaForm

def home(request):
    noticias = Noticia.objects.all()
    return render(request, 'home.html', {'noticias': noticias})

def categoria(request, categoria):
    noticias = Noticia.objects.filter(categoria=categoria)
    return render(request, 'categoria.html', {'noticias': noticias, 'categoria': categoria})

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
def add_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = NoticiaForm()
    return render(request, 'add_noticia.html', {'form': form})

@login_required(login_url='/login')
def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'editar_noticia.html', {'form': form, 'noticia': noticia})

@login_required(login_url='/login')
def excluir_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('admin_dashboard')
    return render(request, 'excluir_noticia.html', {'noticia': noticia})
