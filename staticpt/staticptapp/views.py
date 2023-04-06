from django.shortcuts import render
from . models import Place, Travellers


# Create your views here.
def fun(request):
    obj=Place.objects.all()
    objt=Travellers.objects.all()
    return render(request, 'index.html', {'result':obj, 'results':objt}, )

