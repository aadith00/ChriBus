from django import forms

class BusSearchForm(forms.Form):
    from_city = forms.CharField(max_length=100)
    to_city = forms.CharField(max_length=100)
    date = forms.DateTimeField(required=True)
