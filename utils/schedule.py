def cooling_schedule(t):
    initial_temp = 1000.0
    cooling_rate = 0.95
    return initial_temp * (cooling_rate ** t)

