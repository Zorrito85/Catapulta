class RubberBand:
    def __init__(self, elasticity, length):
        self.elasticity = elasticity
        self.length = length

    def stretch(self, amount):
        self.length += amount

    def release(self):
        return self.elasticity * self.length

    def __str__(self):
        return f"RubberBand(elasticity={self.elasticity}, length={self.length})"