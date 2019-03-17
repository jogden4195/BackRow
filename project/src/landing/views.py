from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):
    return render(request, 'landing/index.html')

def about(request):
    return render(request, 'landing/about.html')

def picker(request):
    return render(request, 'landing/picker.html')

def audience(request):
    return render(request, 'landing/audience.html')

def presentation(request, fileId):
    elink = get_embed_link(fileId)

    return render(request, 'landing/presentation.html', {'elink': elink})

def get_embed_link(file_id):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    import pickle
    import os.path
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request

    SCOPES = ['https://www.googleapis.com/auth/drive']

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v2', credentials=creds)

    # Call the Drive v3 API
    file = service.files().get(fileId=file_id).execute()

    return file.get('embedLink')
