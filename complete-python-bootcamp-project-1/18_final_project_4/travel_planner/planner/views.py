from django.shortcuts import render, redirect
from .forms import ItineraryForm, AirlineForm, HotelForm, PointOfInterestForm
from .models import Itinerary


# def home(request):
#     # Query all itineraries to display them on the home page
#     itineraries = Itinerary.objects.all()
#     return render(request, 'home.html', {'itineraries': itineraries})

def home(request):
    # Query all itineraries to display them on the home page
    itineraries = Itinerary.objects.all()
    
    # Add calculations for each itinerary
    for itinerary in itineraries:
        # Calculate the number of days for the itinerary
        itinerary.num_days = (itinerary.end_date - itinerary.start_date).days

        # Calculate the total hotel cost for the itinerary
        total_hotel_cost = 0
        for hotel in itinerary.hotels.all():
            if hotel.check_in and hotel.check_out:
                nights = (hotel.check_out - hotel.check_in).days
                total_hotel_cost += nights * hotel.cost_per_night
        
        # Add the total hotel cost to the itinerary object (optional)
        itinerary.total_hotel_cost = total_hotel_cost
    
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
