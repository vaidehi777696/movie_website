from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['seats']  # Add more fields as needed
        widgets = {
            'seats': forms.CheckboxSelectMultiple,
        }