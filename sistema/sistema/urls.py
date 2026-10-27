# urls.py: É o "roteador" da aplicação. Ele mapeia os caminhos 
# de URL digitados no navegador e os direciona para as respetivas 
# Views que vão processar e retornar a resposta.

from django.contrib import admin
from django.urls import path
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
