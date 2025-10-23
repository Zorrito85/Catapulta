class PaperClip:
    def __init__(self):
        self.name = "Paper Clip"
        self.strength = 1  # Represents the strength of the paper clip in holding parts together

    def __str__(self):
        return f"{self.name} with strength {self.strength}"