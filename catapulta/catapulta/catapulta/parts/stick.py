class Stick:
    def __init__(self, length, strength):
        self.length = length
        self.strength = strength

    def __str__(self):
        return f"Stick(length={self.length}, strength={self.strength})"