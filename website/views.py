from django.shortcuts import render


def home_page_view(request):
    return render(request, 'website/Home.html')


def exemplos_page_view(request):
    return render(request, 'website/Exemplos.html')


def sobre_page_view(request):
    return render(request, 'website/Sobre.html')
