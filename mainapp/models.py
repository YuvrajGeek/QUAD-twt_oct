from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Links(models.Model):
    name = models.CharField(max_length=256)
    link = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' | ' + self.link + str(self.author)


class VideoConfLinks(models.Model):
    name = models.CharField(max_length=256)
    link = models.URLField()
    platform = models.CharField(max_length=256,  choices=[(
        'Zoom', 'Zoom'), ('Google Meet', 'Google Meet'), ('Jitsi Meet', 'Jitsi Meet'), ('MS Teams', 'MS Teams')])
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' | ' + self.link


class Task(models.Model):
    title = models.CharField(max_length=256)
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " | " + str(self.date_created) + " | " + str(self.complete)


class Question(models.Model):
    title = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    time_posted = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title + "  by  " + str(self.author)

class Answer(models.Model):
    content = models.TextField()
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.writer) + '  answered  ' +  str(self.question)
