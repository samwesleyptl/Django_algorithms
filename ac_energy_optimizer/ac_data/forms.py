# ac_data/forms.py
from django import forms

class OptimizeEnergyForm(forms.Form):
    room_temp = forms.FloatField(label='Room Temperature (°C)', min_value=-50, max_value=50)
    ac_temp = forms.FloatField(label='AC Temperature (°C)', min_value=-50, max_value=50)
    humidity = forms.FloatField(label='Humidity (%)', min_value=0, max_value=100)
