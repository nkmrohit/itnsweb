from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404,HttpRequest,HttpResponse,HttpResponseRedirect
from setting.form import settingForm
from setting.models import settings
from django.utils import timezone
from datetime import datetime
from decimal import Decimal

# Create your views here.
def index(request):
    dataAll = settings.objects.all()
    return  render(request, 'setting/index.html',{'data':dataAll})

def create(request):
    #return HttpResponse("dsafdsa")
    if request.method=='POST':
       
        form = settingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/backend/setting/')
        else:    
            
            return render(request,'setting/create.html',{'form':form})     
    else:
        
        form = settingForm()
        return render(request,'setting/create.html',{'form':form})

def update(request, id):
    instance = get_object_or_404(settings,pk=id)
    form = settingForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        form = settingForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/backend/setting/')
        else:
            form = settingForm(request.POST or None, instance=instance)
            return render(request,'setting/update.html',{'form':form,'id':id})  

    return render(request,'setting/update.html',{'form':form,'id':id}) 
        
def delete(request, id):
    #return HttpResponse(id)
    #id = request.GET['id']
    if id:
        settings.objects.get(id=id).delete()
        return HttpResponseRedirect('/backend/setting/',{'arg':'Successfully Deleted'})   
    return HttpResponseRedirect('/backend/setting/',{'arg':'Some Thing going to wrong'})    