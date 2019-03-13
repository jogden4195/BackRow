from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'landing/index.html')

def picker(request):
    return render(request, 'landing/picker.html')

def audience(request):
    return render(request, 'landing/audience.html')
