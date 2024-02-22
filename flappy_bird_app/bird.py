from .pipes import Pipes


#constants for all instances of Bird that aren't referenced elsewhere
GRAVITY = 0.00125
MAX_VELOCITY = 0.02
JUMP_VELOCITY = -0.0175
JUMP_ANGLE = 20
ANGULAR_VELOCITY = 5


class Bird:
    """The bird."""

    def __init__(self) -> None:
        self.x: float = 0.3
        self.radius: float = 0.04
        self.position: float
        self.velocity: float
        self.angle: int

        self.pipes: Pipes = Pipes()

        self.score: int


    def start_state(self) -> None:
        """Get the bird in a state to start the game.
        
        Set at starting position, set vertical velocity, initialise the pipes.
        """

        self.position = 0.6
        self.velocity = JUMP_VELOCITY
        self.angle = JUMP_ANGLE

        self.pipes.start_state()

        self.score = 0

    def move(self, move: int) -> None:
        """Flap or don't flap.
        
        The argument move should be 0 for doing nothing and 1 for flapping.
        """

        match(move):
            case 0:
                self.velocity += GRAVITY
                self.velocity = min(self.velocity, MAX_VELOCITY)
                if self.velocity >= MAX_VELOCITY / 2:
                    self.angle -= ANGULAR_VELOCITY
                    self.angle = max(self.angle, -90)
            case 1:
                self.velocity = JUMP_VELOCITY
                self.angle = JUMP_ANGLE
        
        self.position += self.velocity
        self.pipes.update()

        #update score if necessary
        front_pipe = self.pipes.items[0]
        if front_pipe.position < self.x and not front_pipe.beaten:
            self.score += 1
            front_pipe.beaten = True

    @property
    def is_dead(self) -> bool:
        """Return True if collided with floor or pipe."""

        #floor
        if self.position + self.radius > 1:
            return True
        
        #first pipe
        for point in self.pipes.items[0].boundary:
            if (point[0] - self.x)**2 + (point[1] - self.position)**2 < self.radius**2:
                return True

        return False