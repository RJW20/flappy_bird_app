import random
from functools import cached_property


#constants for all instances of Pipe
WIDTH = 0.18
MIN_HEIGHT = 0.09
GAP = 0.27
PAN_VELOCITY = -0.006


class Pipe:
    """A pipe that can kill the bird.
    
    Will be initialized with a random height ~U[min_height,1-min_height-gap], and have set width.
    position represents the x-coordinate of the left of the end of the pipe.
    width represents the difference in x-cooridinate from left to right of the end of the pipe.
    height represents the y-coordinate of the end of the top pipe (coordinates are top-down).
    """

    def __init__(self, position: float) -> None:
        self.position: float = position
        self.width: float = WIDTH
        self.height: float = round(random.uniform(MIN_HEIGHT, 1 - MIN_HEIGHT - GAP) * 100) / 100
        self.beaten: bool = False

    @cached_property
    def bottom_height(self) -> float:
        """The y-coordinate of the end of the bottom pipe."""

        return self.height + GAP

    def update(self) -> None:
        """Move pipe by PAN_VELOCITY."""

        self.position += PAN_VELOCITY