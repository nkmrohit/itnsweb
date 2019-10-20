from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404,HttpRequest,HttpResponse,HttpResponseRedirect
from capability.form import capabilityForm
from capability.models import capability
from django.utils import timezone
from datetime import datetime
from decimal import Decimal

# Create your views here.
def index(request):

    col_list =['id','name','image','logo']
    dataAll = capability.objects.all()
    return  render(request, 'capability/index.html',{'data':dataAll})

def create(request):
    #return HttpResponse("dsafdsa")
    if request.method=='POST':
       
        form = capabilityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/backend/capability/')
        else:    
            
            return render(request,'capability/create.html',{'form':form})     
    else:
        
        form = capabilityForm()
        return render(request,'capability/create.html',{'form':form})

def update(request, id):
    instance = get_object_or_404(capability,pk=id)
    form = capabilityForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        form = capabilityForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/backend/capability/')
        else:
            form = capabilityForm(request.POST or None, instance=instance)
            return render(request,'capability/update.html',{'form':form,'id':id})  

    return render(request,'capability/update.html',{'form':form,'id':id}) 
        
def delete(request, id):
    #return HttpResponse(id)
    #id = request.GET['id']
    if id:
        capability.objects.get(id=id).delete()
        return HttpResponseRedirect('/backend/capability/',{'arg':'Successfully Deleted'})   
    return HttpResponseRedirect('/backend/capability/',{'arg':'Some Thing going to wrong'})    