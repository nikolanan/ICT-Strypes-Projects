from django import forms
from .models import Itinerary, Airline, Hotel, PointOfInterest

class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
    hotels = forms.ModelMultipleChoiceField(
        queryset = Hotel.objects.all(),
        required = False,
        widget = forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
    )

    airlines = forms.ModelMultipleChoiceField(
        queryset = Airline.objects.all(),
        required = False,
        widget = forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
    )

    points_of_interest = forms.ModelMultipleChoiceField(
        queryset = PointOfInterest.objects.all(),
        required = False,
        widget = forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
    )

class AirlineForm(forms.ModelForm):
    class Meta:
        model = Airline
        fields = '__all__'
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }

class PointOfInterestForm(forms.ModelForm):
    class Meta:
        model = PointOfInterest
        fields = ['name', 'description', 'location']
