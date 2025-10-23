# filepath: c:\Users\manue\OneDrive\Documentos\Programacion\Catapulta\main.py

from catapulta.catapult import Catapult
from catapulta.enemies.goblin import Goblin

def main():
    # Initialize the catapult
    catapult = Catapult()

    # Create some enemies
    goblin1 = Goblin(health=30, damage=5)
    goblin2 = Goblin(health=25, damage=7)

    # Add parts to the catapult
    catapult.add_part("stick")
    catapult.add_part("rubber_band")
    catapult.add_part("glue")
    catapult.add_part("bottle_cap")
    catapult.add_part("paper_clip")

    # Launch a projectile
    catapult.launch_projectile(weight=10, velocity=20)

    # Simulate enemy actions
    goblin1.attack()
    goblin2.attack()

if __name__ == "__main__":
    main()