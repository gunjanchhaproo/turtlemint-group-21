from django.shortcuts import render,redirect

from turtlemintapp.models import Motor

def home(request):
    return render (request,'turtlemintapp/index.html')

def carSelection(request):
    motorData=Motor.objects.all()
    context={
        'keyposts':motorData
    }
    print(motorData)
    print(context)
    return render(request,'turtlemintapp/carSelection.html', context)
# Create your views here.
