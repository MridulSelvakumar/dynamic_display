from django.shortcuts import render
from app.models import *

# Create your views here.
def dynamic_Topics(request):
    tn=input("enter the topic:")
    NewTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NewTO.save()
    QLOB=Topic.objects.all()
    d={'Q': QLOB }
    return render(request,'dynamic_Topics.html',d)

#def dynamic_webpages(request):
    tn=input("enter the topic:")
    n=input("enter the name:")
    TO=Topic.objects.get(topic_name=tn)
    NewWO=Webpage.objects.get_or_create(topic_name=TO,name=n)[0]
    NewWO.save()
    WLOD=Webpage.objects.all()
    d={'W':WLOD}
    return render(request,'dynamic_webpages.html',d)