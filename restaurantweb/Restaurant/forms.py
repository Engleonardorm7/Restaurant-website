from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields=['first_name', 'last_name','guest_number', 'comment']