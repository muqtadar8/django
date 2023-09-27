from django.shortcuts import render
from .models import Destination

# Create your views here.

def home(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'city of dreams'
    dest1.img = 'destination_1.jpg'
    dest1.price = 800
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'The city of Pearls '
    dest2.img = 'destination_2.jpg'
    dest2.price = 900
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Jaipur'
    dest3.desc = 'Pink cty'
    dest3.img = 'destination_3.jpg'
    dest3.price = 600
    dest3.offer = False

    dests = [dest1,dest2,dest3]



    return render(request,'home.html',{'dests':dests})

