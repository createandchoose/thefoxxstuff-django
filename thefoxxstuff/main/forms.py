from .import Task
from django.forms import ModelForm, fields


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title, task"]