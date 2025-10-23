class Goblin(Enemy):
    def __init__(self, health=30, damage=5, name="Goblin"):
        super().__init__(health, damage, name)
        self.loot = "Gold Coin"

    def attack(self):
        print(f"{self.name} attacks for {self.damage} damage!")

    def take_damage(self, amount):
        super().take_damage(amount)
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.health} health remaining.")