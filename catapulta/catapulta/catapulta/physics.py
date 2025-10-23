def calculate_gravity(mass, height):
    g = 9.81  # acceleration due to gravity in m/s^2
    return mass * g * height

def calculate_force(mass, acceleration):
    return mass * acceleration

def calculate_trajectory(initial_velocity, angle, time):
    import math
    angle_rad = math.radians(angle)
    x = initial_velocity * math.cos(angle_rad) * time
    y = initial_velocity * math.sin(angle_rad) * time - 0.5 * calculate_gravity(1, 1) * time**2
    return x, y