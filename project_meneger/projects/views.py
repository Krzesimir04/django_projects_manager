from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Project
from .forms import *
from django.views.decorators.http import require_POST
# Create your views here.
class Index_view(ListView):
    template_name= 'index.html'
    model=Project

def edit(request,pk):
    if request.method=='POST':
        form=Edit_form(request.POST)
        if form.is_valid():
            project=Project.objects.get(id=pk)
            project.workers.set(form.cleaned_data.get('workers'))    
            Project.objects.filter(id=pk).update(describtion=form.cleaned_data.get('describtion'), name=form.cleaned_data.get('name'), deadline=form.cleaned_data.get('deadline'))
            return redirect('/')
    elif request.method=='GET':
        project=Project.objects.get(id=pk)
        form=Edit_form(instance=project)
        return render(request, 'edit.html', {'form':form})
    
def add(request):
    if request.method=='POST':
        form=Edit_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    elif request.method=='GET':
        form=Edit_form()
        return render(request, 'edit.html', {'form':form})

def delete(request,pk):
    Project.objects.filter(id=pk).delete()
    return redirect('/')