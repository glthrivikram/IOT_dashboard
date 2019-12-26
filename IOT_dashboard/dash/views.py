from django.shortcuts import render
from dash.forms import fieldForm
from dash.forms import dataForm
from django.http import HttpResponse
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
            html = "<html><body>200,ok</body></html>"
            return HttpResponse(html)
    else:
        form = fieldForm()
        return render(request, "newLocation.html", {'form': form})
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
