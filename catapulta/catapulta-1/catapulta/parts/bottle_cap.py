class BottleCap:
    def __init__(self):
        self.material = "plastic"
        self.diameter = 3  # in centimeters

    def get_properties(self):
        return {
            "material": self.material,
            "diameter": self.diameter
        }