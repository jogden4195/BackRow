from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):
    return render(request, 'landing/index.html')

def picker(request):
    return render(request, 'landing/picker.html')

def audience(request):
    return render(request, 'landing/audience.html')

def presentation(request, fileId):
    # return HttpResponse('<h1>Your fileID is ' + fileId + '! </h1>')
    req = requests.get('https://www.googleapis.com/drive/v2/files/{}'.format(fileId))
    if req.status_code == 200:
        elink = req.json().get('embedLink')
    return render(request, 'landing/presentation.html', {'elink': elink})