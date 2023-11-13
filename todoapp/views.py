from django.shortcuts import render, redirect,get_object_or_404
from .models import Todo
from .forms import TodoForm
# Create your views here.
def home(request):
    todo_false = Todo.objects.filter(is_active=False)
    todo_true = Todo.objects.filter(is_active=True)
    todo_false_count = Todo.objects.filter(is_active=False).count()
    todo_true_count = Todo.objects.filter(is_active=True).count()
    if request.method == "POST":
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()
    context = {
        'todo_false': todo_false,
        'todo_true': todo_true,
        'todo_false_count': todo_false_count,
        'todo_true_count': todo_true_count,
        'form': form,
    }
    return render(request, 'home.html', context)
def update_item(request, pk):
    todo_false = Todo.objects.filter(is_active=False)
    todo_true = Todo.objects.filter(is_active=True)
    item = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=item)
    context = {
        'todo_false': todo_false,
        'todo_true': todo_true,
        'form': form,
    }
    return render(request, 'home.html', context)
def delete_item(request, pk):
    item = get_object_or_404(Todo, pk=pk)
    item.delete()
    return redirect('home')

def update_status(request, pk):
    item = get_object_or_404(Todo, pk=pk)
    item.is_active = True
    item.save()
    return redirect('home')