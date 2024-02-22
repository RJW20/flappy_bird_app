from collections import deque

from .pipe import Pipe


#constants for all instances of Pipes that aren't referenced elsewhere
SEPARATOR = 0.6


class Pipes:
    """Double-ended queue containing the pipes."""

    def __init__(self) -> None:
        self.items: deque[Pipe]

    def start_state(self) -> None:
        """Get the pipes in a state to start the game.
        
        Populate deque, set at starting positions.
        """

        self.items = deque([Pipe(0)])

    def update(self) -> None:
        """Move the pipes one frame to the left.
        
        Add pipe to the end of self.items if soon to be visible.
        Remove pipe at beginning of self.items if no longer visible.
        """

        for pipe in self.items:
            pipe.update()

        if (end_pipe_position := self.items[-1].position) < 1:
            self.items.append(Pipe(end_pipe_position + SEPARATOR))

        if self.items[0].position < self.items[0].width * -1:
            self.items.popleft()       