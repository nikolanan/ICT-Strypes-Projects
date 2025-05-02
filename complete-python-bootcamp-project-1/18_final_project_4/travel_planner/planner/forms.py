from django import forms
from .models import Itinerary, Airline, Hotel, PointOfInterest

class ItineraryForm(forms.ModelForm):
    """ Form for creating itineraries.

    :param forms: Django forms module.
    :type forms: django.forms
    """ 
    class Meta:
        """ 
        Meta class for ItineraryForm.
        This class defines the model and fields to be used in the form.
        """  
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
    """Form for creating airlines.

    :param forms: Django forms module.
    :type forms: django.forms
    """    
    class Meta:
        """ 
        Meta class for AirlineForm.
        This class defines the model and fields to be used in the form.
        """ 
        model = Airline
        fields = '__all__'
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class HotelForm(forms.ModelForm):
    """Form for creating hotels.

    :param forms: Django forms module.
    :type forms: django.forms
    """    
    class Meta:
        """
        Class for HotelForm.
        This class defines the model and fields to be used in the form.
        """        
        model = Hotel
        fields = '__all__'
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }

class PointOfInterestForm(forms.ModelForm):
    """Form for creating points of interest.

    :param forms: Django forms module.
    :type forms: django.forms
    """    
    class Meta:
        """
        Class for PointOfInterestForm.
        This class defines the model and fields to be used in the form.
        """       
        model = PointOfInterest
        fields = ['name', 'description', 'location']
