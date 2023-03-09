from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class tasklistview(ListView):
    model=task
    template_name = 'home.html'
    context_object_name= 'Task'

class taskdetailview(DetailView):
    model=task
    template_name = 'detail.html'
    context_object_name= 'Task'

class taskupdateview(UpdateView):
    model=task
    template_name = 'update.html'
    context_object_name= 'Task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class taskdeleteview(DeleteView):
    model=task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def index(request):
    Task1 = task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('Task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date','')
        Task = task(name=name, priority=priority, date=date)
        Task.save()

    return render(request, 'home.html', {'Task': Task1})


# def details(request):
#     return render(request, 'detail.html',)

def delete(request, taskid):
    Task = task.objects.get(id=taskid)
    if request.method == 'POST':
        Task.delete()
        return redirect('/')
    return render(request, 'delete.html')

def update(request,id):
    Task = task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=Task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html',{'f': f,'Task': Task})