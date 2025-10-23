class Catapult:
    def __init__(self):
        self.parts = []
        self.projectiles = []

    def add_part(self, part):
        self.parts.append(part)

    def launch_projectile(self, projectile):
        self.projectiles.append(projectile)
        trajectory = projectile.calculate_trajectory()
        print(f"Launched projectile with trajectory: {trajectory}")

    def get_parts(self):
        return self.parts

    def get_projectiles(self):
        return self.projectiles