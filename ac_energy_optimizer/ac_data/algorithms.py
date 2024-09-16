# ac_data/algorithms.py
def optimize_energy(room_temp, ac_temp, humidity):
    # Simple logic to adjust AC temperature and calculate energy-saving factor
    if room_temp > 25 and humidity > 60:
        new_ac_temp = ac_temp + 1
    elif room_temp < 20:
        new_ac_temp = ac_temp - 1
    else:
        new_ac_temp = ac_temp

    energy_saving_factor = max(0, 1 - abs(new_ac_temp - ac_temp) * 0.05)
    return new_ac_temp, energy_saving_factor
