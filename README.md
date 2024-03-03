# Flappy Bird
A python implementation of the game Flappy Bird using [pygame](https://www.pygame.org/docs/)

## Basic Requirements
1. [Python](https://www.python.org/downloads/)
2. [Poetry](https://python-poetry.org/docs/) for ease of installing the dependencies.

## Getting Started
1. Clone or download the repo `git clone https://github.com/RJW20/flappy_bird_app.git`.
2. Set up the virtual environment with `poetry install`.
3. (Optional) Set your desired screen size in scripts/main.py (try to keep a ratio of about 3:4 for width:height for best perfomance).
4. Run the game with `poetry run main`.
5. Press space to jump and enjoy!

## Note
This was made with the intention of creating an AI for the game using the genetic algorithm as seen [here](https://github.com/RJW20/flappy_bird_ai_genetic_algorithm). As such the game is not polished (i.e. has no start/death screen, doesn't record high score) and uses dimensionless positions in (0,1) so collisions may be slightly off if you play with the width/height too much.
