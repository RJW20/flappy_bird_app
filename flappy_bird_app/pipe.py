import random
from functools import cached_property


#constants for all instances of Pipe that aren't referenced elsewhere
MIN_HEIGHT = 0.05
PAN_VELOCITY = -0.006


class Pipe:
    """A pipe that can kill the bird.
    
    Will be initialized with a random height ~U[min_height,1-min_height-gap], and have set width.
    height represents the y-coordinate of the end of the top pipe (coordinates are top-down).
    width represents the difference in x_cooridinate from left to right of the pipe.
    position represents the x-coordinate of the left of the pipe.
    """

    def __init__(self, position: float) -> None:
        self.position: float = position
        self.width: float = 0.18
        self.gap: float = 0.275
        self.height: float = round(random.uniform(MIN_HEIGHT, 1 - MIN_HEIGHT - self.gap) * 100) / 100

        self.beaten: bool = False

    @cached_property
    def bottom_height(self):
        """The y_coordinate of the end of the bottom pipe."""

        return self.height + self.gap

    def update(self) -> None:
        """Move pipe by PAN_VELOCITY."""

        self.position += PAN_VELOCITY