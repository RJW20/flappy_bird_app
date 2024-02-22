


class Bird:
    """The bird."""

    def __init__(self) -> None:
        pass

    def start_state(self) -> None:
        """Get the bird in a state to start the game.
        
        Set at starting position, set vertical velocity, initialise the pipes.
        """

    def move(self, move: int) -> None:
        """Flap or don't flap.
        
        The argument move should be 0 for doing nothing and 1 for flapping.
        """

    @property
    def is_dead(self) -> bool:
        """Return True if collided with floor or pipe."""