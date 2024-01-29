from django import forms
from .models import Booking

class BusSearchForm(forms.Form):
    from_city = forms.CharField(max_length=100)
    to_city = forms.CharField(max_length=100)
    date = forms.DateTimeField(required=True)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'seat_num']
