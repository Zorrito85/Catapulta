class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def attack(self):
        return self.damage

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        return self.health