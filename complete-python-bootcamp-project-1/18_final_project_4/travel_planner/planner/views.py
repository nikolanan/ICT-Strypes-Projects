from django.shortcuts import render, redirect
from .forms import ItineraryForm, AirlineForm, HotelForm, PointOfInterestForm
from .models import Itinerary


def home(request):
    """Home view for the travel planner application.
    This view is responsible for displaying all itineraries and their details.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML response containing the home page with itineraries.
    :rtype: HttpResponse
    """    
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
    """Create a new itinerary.
    This view handles the creation of a new itinerary using a form.

    :param request: The HTTP request object.
    :type request:  HttpRequest
    :return: A rendered HTML response containing the itinerary creation form.
    :rtype: HttpResponse
    """    
    if request.method == 'POST':
        form = ItineraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItineraryForm()
    return render(request, 'create_itinerary.html', {'form': form})

def create_airline(request):
    """ Create a new airline.
    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML response containing the airline creation form.
    :rtype: HttpResponse
    """    
    if request.method == 'POST':
        form = AirlineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AirlineForm()
    return render(request, 'create_airline.html', {'form': form})

def create_hotel(request):
    """ Create a new hotel.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A rendered HTML response containing the hotel creation form.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HotelForm()
    return render(request, 'create_hotel.html', {'form': form})

def create_point_of_interest(request):
    """ Create a new point of interest.

    :param request: The HTTP request object.
    :type request:  HttpRequest
    :return: A rendered HTML response containing the point of interest creation form.
    :rtype: HttpResponse
    """    
    if request.method == 'POST':
        form = PointOfInterestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PointOfInterestForm()
    return render(request, 'create_point_of_interest.html', {'form': form})
