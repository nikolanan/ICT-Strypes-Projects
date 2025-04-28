from django.contrib import admin
from .models import Airline, Hotel, PointOfInterest, Itinerary

admin.site.register(Airline)
admin.site.register(Hotel)
admin.site.register(PointOfInterest)
admin.site.register(Itinerary)
