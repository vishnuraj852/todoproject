from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Tasks
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.


class TaskListView(ListView):
    model = Tasks
    template_name = 'index.html'
    context_object_name = 'task'



class TaskDetialview(DetailView):
    model = Tasks
    template_name = 'detail.html'
    context_object_name = 'task1'


class TaskUpdateView(UpdateView):
    model = Tasks
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cvbdetail', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Tasks
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

def index(request):
    t = Tasks.objects.all()
    if request.method == 'POST':
        name = request.POST.get("name")
        priority = request.POST.get("priority")
        date = request.POST.get("date")
        tasks = Tasks(name=name, priority=priority, date=date)
        tasks.save()
    return render(request, 'index.html', {'task': t})


def delete(request, taskid):
    if request.method == 'POST':
        task = Tasks.objects.get(id=taskid)
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Tasks.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 'task': task})
