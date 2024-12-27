from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForms

# def task_index(request):
#     tasks = Task.objects.all()
#     return render(request, 'index.html', context={'tasks': tasks})

# def task_create(request):
#     if request.method == 'POST':
#         form = TaskForms(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     return render(request, 'create.html', context={'form': TaskForms})

# def task_update(request, id):
#     task = get_object_or_404(Task, id=id)
#     if request.method == 'POST':
#         form = TaskForms(data=request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     return render(request, 'update.html', context={'form': TaskForms(instance=task)})

# def task_delete(request, id):
#     task = get_object_or_404(Task, id=id)
#     task.delete()
#     return redirect('index')

def task_detail(request, id):
    return render(request, 'detail.html', context={'task': get_object_or_404(Task, id=id)})

from django.views import View

class CreateView(View):
    def get(self, request):
        return render(request, 'create.html', context={'form': TaskForms})

    def post(self, request):
        form = TaskForms(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'create.html', context={'form': TaskForms})

class ListView(View):
    def get(self, request):
        return render(request, 'index.html', context={'tasks': Task.objects.all()})

from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
class UpdateViewTask(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('index')

class DeleteView(View):
    def get(self, request, id):
        get_object_or_404(Task, id=id).delete()
        return redirect('index')


# class DeleteViewTask(DeleteView):
#     model = Task
#     fields = '__all__'
#     template_name = 'delete.html'
#     success_url = reverse_lazy('index')

class DetailView(View):
    def get(self, request, id):
        return render(request, 'detail.html', context={'task': get_object_or_404(Task, id=id)})