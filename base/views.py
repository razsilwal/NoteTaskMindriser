from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Note, NoteType
from .forms import NoteTypeForm, NoteForm, UserForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
# Create your views here.

def home(request):
    note_obj = Note.objects.all().order_by('id')
    data = {
        'notes':note_obj
    }
    return render(request, 'home.html', context=data)

# view all the notetype 
def notetype(request):
    note_obj = NoteType.objects.all()
    data = {
        'notetypes':note_obj
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
    if request.method == 'POST':
        notetype_form =  NoteTypeForm(data=request.POST)
        if notetype_form.is_valid():
            notetype_form.save()
            messages.success(request, 'Note type is created ')
            return redirect('notetype')
        
        else:
            messages.error(request, notetype_form.errors)

    notetype_form = NoteTypeForm()
    data = {
        'form' : notetype_form
        }
    return render(request, 'create_notetype.html', context=data)

def edit_note_view(request, pk):
    note_obj = Note.objects.get(id=pk)
    if request.method == 'POST':
        note_form_obj = NoteForm(data=request.POST, instance=note_obj)
        if note_form_obj.is_valid():
            note_form_obj.save()
            messages.success(request, 'Note updated sucessfully ')
            return redirect('home')
        
        else:
            messages.error(request, note_form_obj.errors)

    note_form_obj = NoteForm(instance=note_obj)
    data = {
        'form':note_form_obj
    }
    return render(request, 'edit_note.html', context=data)

def delete_note(request, pk):
    note_obj = Note.objects.get(id=pk)
    note_obj.delete()
    messages.success(request, 'Note deleted sucessfully ')
    return redirect('home')

def delete_all_note(request):
    note_obj_all = Note.objects.all()
    note_obj_all.delete()
    messages.success(request, 'All note deleted sucessfully ')
    return redirect('home')


# Edited of NoteType 
def edit_notetype(request, pk):
    notetype_obj = NoteType.objects.get(id=pk)
    if request.method == 'POST':
        notetype_form_obj = NoteTypeForm(data=request.POST, instance=notetype_obj)
        if notetype_form_obj.is_valid():
            notetype_form_obj.save()
            messages.success(request, 'Notetype Updated Sucessfully !! ')
            return redirect('notetype')
        else:
            messages.error(request, notetype_form_obj.errors)

    notetype_form_obj = NoteTypeForm(instance=notetype_obj)
    data = {
        'form': notetype_form_obj
    }
    return render(request, 'edit_notetype.html', context = data)

def delete_notetype(request, pk):
    notetype_obj = NoteType.objects.get(id=pk)
    notetype_obj.delete()
    messages.success(request, 'Notetype deleted sucessfully ')
    return redirect('notetype')

def register_view(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        hash_password = make_password(password)
        data = request.POST.copy()
        data['password'] = hash_password
        user_form_obj = UserForm(data=data)
        if user_form_obj.is_valid():
            user_form_obj.save()
            messages.success(request, 'Register Sucessfully')
            return redirect('home')
        else:
            messages.error(request, user_form_obj.errors)
    
    user_form_obj  = UserForm()
    data = {
        'form':user_form_obj
    }
    return render(request, 'register.html', context=data)

