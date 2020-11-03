from django import forms
from .models import Links, VideoConfLinks, Task


class LinkForm(forms.ModelForm):
    class Meta:
        model = Links
        fields = ('name', 'link', 'author')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What do you wanna call it?'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'value': '', 'type': 'hidden'}),
        }


class VideoConfLinksForm(forms.ModelForm):
    class Meta:
        model = VideoConfLinks
        fields = ('name', 'link', 'platform', 'author')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title...'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
            'platform': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Platform'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'value': '', 'type': 'hidden'}),
        }


class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Name...'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'value': '', 'type': 'hidden'}),
        }
