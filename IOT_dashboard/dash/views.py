from django.shortcuts import render
from dash.forms import fieldForm
from dash.forms import dataForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dash.models import data
from dash.models import feild

# Create your views here.
def home(request):
    return render(request,"home.html")

def newLocation(request):
    if request.method == 'POST':
        print(request.POST)
        # create a form instance and populate it with data from the request:
        form = fieldForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            p =form.save()
            p.save()
            html = "<html><body<br><br><center>LOCATION REGISTERED</center></body></html>"
            return HttpResponse(html)
    else:
        form = fieldForm()
        return render(request, "newLocation.html", {'form': form})
@csrf_exempt
def newData(request):
    if request.method == 'POST':
        print(request.POST)
        # create a form instance and populate it with data from the request:
        form = dataForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            p =form.save()
            p.save()
            html = "<html><body>200,ok</body></html>"
            return HttpResponse(html)
    else:
        form = dataForm()
        return render(request, "newData.html", {'form': form})

def liveStatus(request):
    objs = feild.objects.all()
    context={
    'object_info':objs
    }
    return render(request, "list.html", context)

def liveStatusSpecific(request, oid):
    obj = data.objects.filter(lId=oid).latest()
    loc = feild.objects.filter(lId=oid)
    loc =str(loc[0])
    loc = loc.split(':')[1]
    context={
      'object':obj,
      'loc': loc
    }
    return render(request, "display.html", context)