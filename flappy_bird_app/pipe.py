import random
from functools import cached_property


#constants for all instances of Pipe that aren't referenced elsewhere
MIN_BODY_HEIGHT = 0.09
PAN_VELOCITY = -0.006


class Pipe:
    """A pipe that can kill the bird.
    
    Will be initialized with a random height ~U[min_height,1-min_height-gap], and have set width.
    position represents the x-coordinate of the left of the end of the pipe.
    width represents the difference in x-cooridinate from left to right of the end of the pipe.
    gap represents the difference in y-coordiante from the end of the top and bottom pipes.
    body_height represents the y-coordinate of the end of the body of the top pipe (coordinates are top-down).
    """

    def __init__(self, position: float) -> None:
        self.position: float = position
        self.width: float = 0.18
        self.gap: float = 0.275
        self.end_height = 0.06
        self.body_height: float = round(random.uniform(MIN_BODY_HEIGHT, 1 - MIN_BODY_HEIGHT - self.end_height - self.gap) * 100) / 100

        self.beaten: bool = False

    @cached_property
    def body_width(self) -> float:
        """The difference in x-coordinate from left to right of the body of the pipe."""

        return self.width * 0.98

    @cached_property
    def height(self) -> float:
        """The y-coordinate of the end of the top pipe."""

        return self.body_height + self.end_height

    @cached_property
    def bottom_height(self) -> float:
        """The y-coordinate of the end of the bottom pipe."""

        return self.height + self.gap
    
    @cached_property
    def bottom_body_height(self) -> float:
        """The y-coordinate of the end of the bottom pipe's body."""

        return self.bottom_height + self.end_height

    def update(self) -> None:
        """Move pipe by PAN_VELOCITY."""

        self.position += PAN_VELOCITY