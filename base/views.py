from django.shortcuts import render
from django.http import HttpResponse
from . models import Note

# Create your views here.

def home(request):
    note_obj = Note.objects.all().order_by('id')
    data = {
        'notes':note_obj
    }
    return render(request, 'home.html', context=data)

def notetype(request):
    note_obj = Note.objects.all().order_by('id')
    data = {
        'notetype':note_obj
    }
    return render(request, 'notetype.html', context=data)

def note(request):
    return render(request, 'create_note.html', context=None)