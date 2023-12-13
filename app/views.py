from django.shortcuts import render
from app.models import *

# Create your views here.
def dynamic_Topics(request):
    QLOB=Topic.objects.all()
    d={'Q':QLOB}
    return render(request,'dynamic_Topics.html',d)

def dynamic_webpages(request):
    WLOD=Webpage.objects.all()
    d={'W':WLOD}
    return render(request,'dynamic_webpages.html',d)