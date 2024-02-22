import random


#constants for all instances of Pipe that aren't referenced elsewhere
MIN_HEIGHT = 0.05
PAN_VELOCITY = -0.005


class Pipe:
    """A pipe that can kill the bird."""

    def __init__(self, position: float) -> None:
        self.position: float = position
        self.width: float = 0.18
        self.gap: float = 0.28
        self.height: float = round(random.uniform(MIN_HEIGHT, 1 - MIN_HEIGHT - self.gap) * 100) / 100

    def update(self) -> None:
        """Move pipe by PAN_VELOCITY."""

        self.position += PAN_VELOCITY