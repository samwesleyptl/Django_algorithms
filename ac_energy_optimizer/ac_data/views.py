from django.shortcuts import render

# Create your views here.
# ac_data/views.py
from .models import ACData
from .algorithms import optimize_energy

def ac_dashboard(request):
    # Generate a list of 10 random AC data sets
    ac_data_list = [ACData() for _ in range(10)]
    processed_data = []

    for data in ac_data_list:
        room_temp = data.room_temperature
        ac_temp = data.ac_temperature
        humidity = data.humidity

        # Apply the optimization algorithm
        new_ac_temp, energy_saving_factor = optimize_energy(room_temp, ac_temp, humidity)

        processed_data.append({
            "room_temp": room_temp,
            "ac_temp": ac_temp,
            "new_ac_temp": new_ac_temp,
            "energy_saving_factor": energy_saving_factor,
        })

    return render(request, "ac_data/dashboard.html", {"data": processed_data})
# ac_data/views.py
from django.shortcuts import render
from .forms import OptimizeEnergyForm
from .algorithms import optimize_energy

def optimize_energy_view(request):
    if request.method == 'POST':
        form = OptimizeEnergyForm(request.POST)
        if form.is_valid():
            room_temp = form.cleaned_data['room_temp']
            ac_temp = form.cleaned_data['ac_temp']
            humidity = form.cleaned_data['humidity']

            # Call the optimize_energy function with the form data
            new_ac_temp, energy_saving_factor = optimize_energy(room_temp, ac_temp, humidity)

            # Pass the results to the template
            return render(request, 'optimize_result.html', {
                'new_ac_temp': new_ac_temp,
                'energy_saving_factor': energy_saving_factor,
                'form': form
            })
    else:
        form = OptimizeEnergyForm()

    return render(request, 'optimize_energy.html', {'form': form})
