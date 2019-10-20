from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404,HttpRequest,HttpResponse,HttpResponseRedirect
from services.form import servicesForm
from services.models import servicess
from django.utils import timezone
from datetime import datetime
from decimal import Decimal

# Create your views here.
def index(request):
    dataAll = servicess.objects.all()
    return  render(request, 'services/index.html',{'data':dataAll})

def create(request):
    #return HttpResponse("dsafdsa")
    if request.method=='POST':
       
        form = servicesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/backend/services/')
        else:    
            
            return render(request,'services/create.html',{'form':form})     
    else:
        
        form = servicesForm()
        return render(request,'services/create.html',{'form':form})

def update(request, id):
    instance = get_object_or_404(servicess,pk=id)
    form = servicesForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        form = servicesForm(request.POST or None, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/backend/services/')
        else:
            form = servicesForm(request.POST or None, instance=instance)
            return render(request,'services/update.html',{'form':form,'id':id})  

    return render(request,'services/update.html',{'form':form,'id':id}) 
        
def delete(request, id):
    #return HttpResponse(id)
    #id = request.GET['id']
    if id:
        servicess.objects.get(id=id).delete()
        return HttpResponseRedirect('/backend/services/',{'arg':'Successfully Deleted'})   
    return HttpResponseRedirect('/backend/services/',{'arg':'Some Thing going to wrong'})    