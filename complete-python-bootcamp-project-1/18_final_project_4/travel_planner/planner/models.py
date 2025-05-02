from django.db import models

class Airline(models.Model):
    """
    Model representing an airline.
    """
    name = models.CharField(max_length=255)
    flight_number = models.CharField(max_length=50)
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.name} ({self.flight_number})| Departs: {self.departure_time.strftime('%Y-%m-%d %H:%M:%S')}| Arrives: {self.arrival_time.strftime('%Y-%m-%d %H:%M:%S')}"


class Hotel(models.Model):
    """
    Model representing a hotel. Keeeps track of the hotel name, address,
    check-in and check-out dates, and cost per night.
    """
    name = models.CharField(max_length=255)
    address = models.TextField()
    check_in = models.DateField()
    check_out = models.DateField()
    cost_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name}| Check in: {self.check_in}| Checkout: {self.check_out}"

class PointOfInterest(models.Model):
    """
    A model representing interesting places to visit.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Itinerary(models.Model):
    """
    A model representing a travel itinerary.
    It is the central part of the travel planner application.
    This models is at the center of the database and connects all the other models.
    (the center of a star in the database diagram)
    """
    title = models.CharField(max_length=255)
    airlines = models.ManyToManyField(Airline, blank=True)
    hotels = models.ManyToManyField(Hotel, blank=True)
    points_of_interest = models.ManyToManyField(PointOfInterest, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.title}"
