from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('categoria/<str:categoria>/', views.categoria, name='categoria'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add/', views.add_noticia, name='add_noticia'),
    path('editar/<int:pk>/', views.editar_noticia, name='editar_noticia'),  # Ajuste de id para pk
    path('excluir/<int:pk>/', views.excluir_noticia, name='excluir_noticia'),  # Ajuste de id para pk
    path('noticia/<int:pk>/', views.noticia, name='noticia'),  # Rota para página de notícia completa
    path('destacar/<int:pk>/', views.destacar_noticia, name='destacar_noticia'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
