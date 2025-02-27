"""
URL configuration for almoxarifado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.urls import path, re_path
from ferramentas.views import FerramentaViewSet
from funcionario.views import FuncionarioViewSet
from estoque.views import LogSaidaViewSet, LogEntradaViewSet

ferramenta_list = FerramentaViewSet.as_view({'get': 'list', 'post': 'create'})
ferramenta_url = re_path(r'^ferramentas/$', ferramenta_list, name='ferramenta-list')

funcionario_list = FuncionarioViewSet.as_view({'get': 'list', 'post': 'create'})
funcionario_url = re_path(r'^funcionarios/$', funcionario_list, name='funcionario-list')

saida_list = LogSaidaViewSet.as_view({'get': 'list', 'post': 'create'})
saida_url = re_path(r'^saida/$', saida_list, name='saida-list')

entrada_list = LogEntradaViewSet.as_view({'get': 'list', 'post': 'create'})
entrada_url = re_path(r'^entrada/$', entrada_list, name='entrada-list')

urlpatterns = [
    path('admin/', admin.site.urls),
] + [ferramenta_url] + [funcionario_url] + [entrada_url] + [saida_url]

