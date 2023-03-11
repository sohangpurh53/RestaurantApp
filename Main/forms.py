from django import forms
from .models import Booking
"""Form definition for MODELNAME."""

class BookingForm(forms.ModelForm):
    class Meta:
            model = Booking
            fields = '__all__'
