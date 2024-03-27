from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['title', 'description', 'important']
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Write title'}),
      'description': forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Write description'}),
      'important': forms.CheckboxInput(attrs={'class': 'form-check-input text-center mb-3 display-5'}),
    }