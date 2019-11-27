"""estoque URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cerveja.views import index,produto_lista, produto_novo, produto_delete, produto_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('produto_lista/',produto_lista,name='produto_lista'),
    path('produto_novo/',produto_novo,name='produto_novo'),
    path('produto_delete/<int:pk>/',produto_delete,name='produto_delete'),
    path('produto_edit/<int:pk>/',produto_edit,name='produto_edit'),
    path('saida/', include('notaSaida.urls', namespace='notaSaida')),
    path('analise/', include('analise.urls', namespace='analise')),
]
