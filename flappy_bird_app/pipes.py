from collections import deque

from .pipe import Pipe


class Pipes:
    """Double-ended queue containing the pipes."""

    def __init__(self) -> None:
        self.items: deque[Pipe]

    def start_state(self) -> None:
        """Get the pipes in a state to start the game.
        
        Populate deque, set at starting positions.
        """

    def update(self) -> None:
        """Move the pipes one frame to the left.
        
        Add pipe to the end of self.items if soon to be visible.
        Remove pipe at beginning of self.items if no longer visible.
        """