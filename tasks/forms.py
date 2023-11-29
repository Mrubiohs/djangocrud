from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Escribe un titulo'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder': 'Escribe una desc'}),
            'important' : forms.CheckboxInput(attrs={'class' : 'form-check-imput m-auto mb-1'})
        }