from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm, TodoUpdateform


# Create your views here.


def home(request):
    all = Todo.objects.all()
    return render(request, 'Home.html', context={'todo': all})


def detail(request, todo_id):
    det = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', context={'todo': det})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, "Todo deleted successfully")
    return redirect('Home')


def create(request):
    if request.method == "POST":
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd["title"], body=cd["body"], created=cd["created"])
            messages.success(request, "Todo added successfully", "success")
            return redirect("Home")
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', context={"forms": form})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        form = TodoUpdateform(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("detail", todo_id)

    else:
        form = TodoUpdateform(instance=todo)
    return render(request, 'update.html', context={"form": form})
