from django.shortcuts import render,Http404,HttpResponse

# Create your views here.
def index(request):
    return  render(request, 'authuser/index.html',{'data':'dsafdsa'})