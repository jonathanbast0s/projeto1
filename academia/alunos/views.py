from django.shortcuts import render
from django.http import HttpResponse

def sobre(request):
    return HttpResponse("Sistema de Controle Acadêmico")