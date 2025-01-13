from django.forms import ModelForm
from .models import NoteType
from django import forms

class NoteTypeForm(ModelForm):
    class Meta:
        model = NoteType
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            }