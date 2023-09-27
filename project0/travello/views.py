from django.shortcuts import render
from .models import Destination

# Create your views here.

def home(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'city of dreams'
    dest1.img = 'mumbaiijpg.jpg'
    dest1.price = 800

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'The city of Pearls '
    dest2.img = 'hyd.jpg'
    dest2.price = 900

    dest3 = Destination()
    dest3.name = 'Jaipur'
    dest3.desc = 'Pink cty'
    dest3.img = 'pune.jpg'
    dest3.price = 600



    return render(request,'home.html',{'dest1': dest1, 'dest2': dest2, 'dest3': dest3})

