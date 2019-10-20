from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404,HttpRequest,HttpResponse,HttpResponseRedirect
from feedback.form import feedbackForm
from feedback.models import feedbacks
from django.utils import timezone
from datetime import datetime
from decimal import Decimal

# Create your views here.
def index(request):

    dataAll = feedbacks.objects.all()
    return  render(request, 'feedback/index.html',{'data':dataAll})

def create(request):
    #return HttpResponse("dsafdsa")
    if request.method=='POST':
       
        form = feedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/backend/feedback/')
        else:    
            
            return render(request,'feedback/create.html',{'form':form})     
    else:
        
        form = feedbackForm()
        return render(request,'feedback/create.html',{'form':form})

def update(request, id):
    instance = get_object_or_404(feedbacks,pk=id)
    form = feedbackForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        form = feedbackForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/backend/feedback/')
        else:
            form = feedbackForm(request.POST or None, instance=instance)
            return render(request,'feedback/update.html',{'form':form,'id':id})  

    return render(request,'feedback/update.html',{'form':form,'id':id}) 
        
def delete(request, id):
    #return HttpResponse(id)
    #id = request.GET['id']
    if id:
        feedbacks.objects.get(id=id).delete()
        return HttpResponseRedirect('/backend/feedback/',{'arg':'Successfully Deleted'})   
    return HttpResponseRedirect('/backend/feedback/',{'arg':'Some Thing going to wrong'})    