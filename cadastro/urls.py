from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('pesquisa_string/', views.pesquisa_string, name='pesquisa_string'),
    path('novapesquisa/', views.novapesquisa, name='novapesquisa'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
    path('pesquisa_numero/', views.pesquisa_numero, name='pesquisa_numero'),
    path('editar_cadastro/<int:variavel>/', views.editar_cadastro,
         name='editar_cadastro'),
    path('excluir/<int:variavel>/', views.excluir, name='excluir'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.logout, name='logout'),
    path('upload/', views.upload, name='upload'),
    path('anexo/<int:id>/', views.anexo, name='anexo'),
    path('delete_images/<int:id>/', views.delete_images, name='delete_images')
]
