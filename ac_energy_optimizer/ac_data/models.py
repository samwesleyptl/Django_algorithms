from django.db import models

# Create your models here.
# ac_data/models.py
import random

class ACData:
    def __init__(self):
        self.room_temperature = random.uniform(18.0, 30.0)  # Random room temperature (°C)
        self.ac_temperature = random.uniform(16.0, 26.0)  # Random AC set temperature (°C)
        self.humidity = random.uniform(30, 80)  # Random humidity percentage
        self.energy_consumption = random.uniform(1.0, 5.0)  # Random energy consumption (kWh)

    def __str__(self):
        return f"Room Temp: {self.room_temperature}, AC Temp: {self.ac_temperature}, Humidity: {self.humidity}"
