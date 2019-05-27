from django.shortcuts import render, HttpResponse

def index(request):
    context = {'msg': 'Bold'}
    return render(request, 'rango/index.html', context)


def about(request):
    context = {'msg': 'Bold'}
    return render(request, 'rango/about.html', context)