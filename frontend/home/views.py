from django.shortcuts import render,Http404,HttpResponse
from slider.models import sliders
from services.models import servicess
from setting.models import settings
# Create your views here.
def index(request):
    sliderData = sliders.objects.all()
    servicesData = servicess.objects.all()
    settingssData = settings.objects.all()
    return  render(request, 'home/index.html',{'sliderData':sliderData,'servicesData':servicesData,'settingsData':settings})