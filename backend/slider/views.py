from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404,HttpRequest,HttpResponse,HttpResponseRedirect
from slider.form import sliderForm
from slider.models import sliders
from django.utils import timezone
from datetime import datetime
from decimal import Decimal

# Create your views here.
def index(request):
    dataAll = sliders.objects.all()
    return  render(request, 'slider/index.html',{'data':dataAll})

def create(request):
    #return HttpResponse("dsafdsa")
    if request.method=='POST':
       
        form = sliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/backend/slider/')
        else:    
            
            return render(request,'slider/create.html',{'form':form})     
    else:
        
        form = sliderForm()
        return render(request,'slider/create.html',{'form':form})

def update(request, id):
    instance = get_object_or_404(sliders,pk=id)
    form = sliderForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        form = sliderForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/backend/slider/')
        else:
            form = sliderForm(request.POST or None, instance=instance)
            return render(request,'slider/update.html',{'form':form,'id':id})  

    return render(request,'slider/update.html',{'form':form,'id':id}) 
        
def delete(request, id):
    #return HttpResponse(id)
    #id = request.GET['id']
    if id:
        sliders.objects.get(id=id).delete()
        return HttpResponseRedirect('/backend/slider/',{'arg':'Successfully Deleted'})   
    return HttpResponseRedirect('/backend/slider/',{'arg':'Some Thing going to wrong'})    