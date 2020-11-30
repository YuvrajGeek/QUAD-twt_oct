from django import forms
from .models import Links, VideoConfLinks, Task, Question, Answer


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

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Question'}),
            'author': forms.TextInput(attrs={'id': 'username', 'type': 'hidden'}),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content', 'question', 'writer')
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Answer Here'}),
            'question': forms.TextInput(attrs={'id': 'question', 'type': 'hidden'}),
            'writer': forms.TextInput(attrs={'id': 'username', 'type': 'hidden'}),             
        }
