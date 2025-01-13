from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Note, NoteType
from .forms import NoteTypeForm
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
    if request.method == 'POST':
        name  = request.POST.get('name')
        description = request.POST.get('description')
        type = request.POST.get('type')

        note_type = NoteType.objects.get(id=type)

        Note.objects.create(name=name, description = description, type=note_type)

        return redirect('home')

    notetype_obj = NoteType.objects.all()
    data = {
        'notetypes':notetype_obj
    }
    return render(request, 'create_note.html', context=data)

def create_notetype(request):
    notetye_form = NoteTypeForm()
    data = {
        'form' : notetye_form
        }
    return render(request, 'create_notetype.html', context=data)