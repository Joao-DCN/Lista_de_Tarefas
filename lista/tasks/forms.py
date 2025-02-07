from crispy_forms.helper import FormHelper
from django import forms
from .models import Task

class TaskFrom(forms.ModelForm):
    class Meta:    
        model = Task
        fields = ('title','description')

class EditTaskFrom(forms.ModelForm):
    class Meta:    
        model = Task
        fields = ('title','description', 'status')