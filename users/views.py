from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import path
from .forms import Form
from .models import Contact
# Create your views here.
def list(request):
    conlist=Contact.objects.all()
    return render(request, 'index.html', {'contacts': conlist})
def create(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = Form()
    return render(request, 'c.html', {'form': form})
    return HttpResponse('create')
def update(request,id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        form = Form(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = Form(instance=contact)
    return render(request, 'c.html', {'form': form})

def delete(request,id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('list')
    return render(request, 'd.html', {'contact': contact})
