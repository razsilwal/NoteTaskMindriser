from django.forms import ModelForm
from .models import NoteType, Note
from django import forms
from django.contrib.auth.models import User

class NoteTypeForm(ModelForm):
    class Meta:
        model = NoteType
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            }
        

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'type','description']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control p-2 mb-4'}), 
            'type': forms.Select(attrs={'class':'form-select mb-4'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control p-2 mb-4'}), 
            'password': forms.PasswordInput(attrs={'class':'form-control mb-4'}),
            }
