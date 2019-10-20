from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404,HttpRequest,HttpResponse,HttpResponseRedirect
from portfolio.form import portfolioForm
from portfolio.models import portfolios
from django.utils import timezone
from datetime import datetime
from decimal import Decimal

# Create your views here.
def index(request):
    dataAll = portfolios.objects.all()
    return  render(request, 'portfolio/index.html',{'data':dataAll})

def create(request):
    #return HttpResponse("dsafdsa")
    if request.method=='POST':
       
        form = portfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/backend/portfolio/')
        else:    
            
            return render(request,'portfolio/create.html',{'form':form})     
    else:
        
        form = portfolioForm()
        return render(request,'portfolio/create.html',{'form':form})

def update(request, id):
    instance = get_object_or_404(portfolios,pk=id)
    form = portfolioForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        form = portfolioForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/backend/portfolio/')
        else:
            form = portfolioForm(request.POST or None, instance=instance)
            return render(request,'portfolio/update.html',{'form':form,'id':id})  

    return render(request,'portfolio/update.html',{'form':form,'id':id}) 
        
def delete(request, id):
    #return HttpResponse(id)
    #id = request.GET['id']
    if id:
        portfolios.objects.get(id=id).delete()
        return HttpResponseRedirect('/backend/portfolio/',{'arg':'Successfully Deleted'})   
    return HttpResponseRedirect('/backend/portfolio/',{'arg':'Some Thing going to wrong'})    