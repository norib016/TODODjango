from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):     ##TaskForm is the name of our form and modelform is what django works with 

    class Meta:
        model = Task                ##we tell django which model should we use
        fields = '__all__'          ##fields should end up in our form
