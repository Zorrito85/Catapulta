class Projectile:
    def __init__(self, weight, velocity):
        self.weight = weight
        self.velocity = velocity

    def calculate_trajectory(self, angle):
        import math
        g = 9.81  # acceleration due to gravity in m/s^2
        angle_rad = math.radians(angle)
        trajectory = (self.velocity ** 2 * math.sin(2 * angle_rad)) / g
        return trajectory

    def __str__(self):
        return f"Projectile(weight={self.weight}, velocity={self.velocity})"