from django.shortcuts import render, redirect
import random
from .forms import LinkForm, VideoConfLinksForm, TodoForm
from .models import Links, VideoConfLinks, Task
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def error_404_view(request, exception):
    return redirect('home')


def home(request):
    links = Links.objects.all()
    tasks = Task.objects.all()
    videoconf = VideoConfLinks.objects.all()
    quotes = [
        'Focus on being productive instead of being busy.',
        'Your goal is no longer to get more done, but rather to have less to do.',
        'Oh God, you’ve got to do this today.',
        'Glory lies in the attempt to reach one’s goal and not in reaching it',
        'The secret of getting ahead is getting started.',
        'All our dreams can come true, if we have the courage to pursue them.',
        'No one is perfect - that\'s why pencils have erasers',
        'Life is what happens when you\'re busy making other plans.',
    ]
    length = len(quotes)
    selected_quote = quotes[random.randint(0, length-1)]
    context = {'quote': selected_quote, 'links': links,
               'tasks': tasks, 'videoconf': videoconf}
    return render(request, 'home.html', context=context)


def LinksView(request):
    links = Links.objects.all()
    form = LinkForm()
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/links')

    context = {'form': form, 'links': links}

    return render(request, 'links.html', context)


@login_required
def deleteLink(request, pk):
    item = Links.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/links')

    context = {'item': item}
    return render(request, 'delete.html', context)


def VideoConfView(request):
    links = VideoConfLinks.objects.all()
    form = VideoConfLinksForm()
    if request.method == 'POST':
        form = VideoConfLinksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/conferences')
    context = {'form': form, 'links': links}
    return render(request, 'videoconf.html', context)


@login_required
def deleteVideoConfLink(request, pk):
    item = VideoConfLinks.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/conferences')

    context = {'item': item}
    return render(request, 'delete.html', context)


def TodoView(request):
    tasks = Task.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo')
    context = {'form': form, 'tasks': tasks}
    return render(request, 'todo.html', context)


@login_required
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TodoForm(instance=task)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/todo')

    context = {'form': form, 'task': task}

    return render(request, 'update_task.html', context)


@login_required
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/todo')

    context = {'item': item}
    return render(request, 'delete.html', context)


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
