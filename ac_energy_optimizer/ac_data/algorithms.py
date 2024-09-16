# ac_data/algorithms.py
def optimize_energy(room_temp, ac_temp):
    if ac_temp < 26:
        if room_temp > 25:
            mode = "Cool"
            setpoint = room_temp + 1
        elif room_temp < 25:
            mode = "Cool"
            setpoint = ac_temp + 1
        else:
            mode = "Cool"
            setpoint = ac_temp
    else:
        mode = "Fan"
        setpoint = None  # Fan mode doesn't require a setpoint temperature


    energy_saving_factor = max(0, 1 - abs(setpoint - ac_temp) * 0.05)
    return setpoint, energy_saving_factor
