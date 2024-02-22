import random
from functools import cached_property


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

        self.beaten: bool = False

    def update(self) -> None:
        """Move pipe by PAN_VELOCITY."""

        self.position += PAN_VELOCITY

    @property
    def x_range(self) -> list[float]:
        """List containing the x coordinates of the ends of the pipe."""

        return [x/100 for x in range(round(self.position * 100), round((self.position + self.width) * 100) + 1)]
    
    @cached_property
    def y_range(self) -> list[float]:
        """List containing the y coordinates of the left edges of the pipe."""

        return [y/100 for y in range(1, 100) if y <= self.height * 100 or y >= (self.height + self.gap) * 100]
    
    @property
    def boundary(self) -> None:
        """Set of points constituting the boundary of the pipe.
        
        Includes the left edge and the ends of the top and bottom pipe.
        """

        return [(x, self.height) for x in self.x_range] + \
               [(x, self.height + self.gap) for x in self.x_range] + \
               [(self.position, y) for y in self.y_range]
    
