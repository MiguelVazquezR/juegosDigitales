from django.shortcuts import render, HttpResponse


def inicio(request):
    contexto = {}
    return render(request,"index.html", contexto)