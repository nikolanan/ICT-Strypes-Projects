from django.shortcuts import render, redirect
from .forms import ItineraryForm, AirlineForm, HotelForm, PointOfInterestForm
from .models import Itinerary


def home(request):
    # Query all itineraries to display them on the home page
    itineraries = Itinerary.objects.all()
    return render(request, 'home.html', {'itineraries': itineraries})

def create_itinerary(request):
    if request.method == 'POST':
        form = ItineraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItineraryForm()
    return render(request, 'create_itinerary.html', {'form': form})

def create_airline(request):
    if request.method == 'POST':
        form = AirlineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AirlineForm()
    return render(request, 'create_airline.html', {'form': form})

def create_hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HotelForm()
    return render(request, 'create_hotel.html', {'form': form})

def create_point_of_interest(request):
    if request.method == 'POST':
        form = PointOfInterestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PointOfInterestForm()
    return render(request, 'create_point_of_interest.html', {'form': form})
