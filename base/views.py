from django.shortcuts import render
from django.http import HttpResponse
from . models import Note, NoteType

# Create your views here.

def home(request):
    note_obj = Note.objects.all().order_by('id')
    data = {
        'notes':note_obj
    }
    return render(request, 'home.html', context=data)

def notetype(request):
    note_obj = NoteType.objects.all()
    data = {
        'notetype':note_obj
    }
    return render(request, 'notetype.html', context=data)

def createNote(request):
    notetype_obj = NoteType.objects.all()
    data = {
        'notetypes':notetype_obj
    }
    return render(request, 'create_note.html', context=data)