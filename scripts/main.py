from typing import Iterable, Any

import pygame

from flappy_bird_app import Bird
import flappy_bird_app.pipe as pipe


def custom_cycle(items: Iterable[Any], count: int) -> Any:
    """Performs like itertools.cycle except yields each element count times."""

    saved = []
    for item in items:
        for _ in range(count):
            yield item
        saved.append(item)
    while saved:
        for item in saved:
            for _ in range(count):
                yield item


def main() -> None:

    #pygame setup
    width = 480
    game_height = 620
    floor_height = 0.04 * game_height
    screen = pygame.display.set_mode((width, game_height + floor_height))
    pygame.display.set_caption("Flappy Bird")
    pygame.font.init()
    font_height = int(0.08 * game_height)
    font = pygame.font.Font(pygame.font.get_default_font(), font_height)
    clock = pygame.time.Clock()
    running = True
    dt = 0

    #initialise the bird
    bird = Bird()
    bird.start_state()
    bird_sprites = [pygame.image.load('resources/bird_1.bmp'), pygame.image.load('resources/bird_2.bmp'), pygame.image.load('resources/bird_3.bmp')]
    bird_sprites = [pygame.transform.scale(bird_sprite, (bird.radius * 8/3 * game_height, bird.radius * 2 * game_height)) for bird_sprite in bird_sprites]
    bird_sprite_numbers = custom_cycle([0, 1, 2, 1], 5)

    #prepare the pipe
    pipe_top_sprite = pygame.image.load('resources/pipe_top.bmp')
    pipe_bottom_sprite = pygame.image.load('resources/pipe_bottom.bmp')
    pipe_top_sprite = pygame.transform.scale(pipe_top_sprite, (pipe.WIDTH * width, (1 - pipe.MIN_HEIGHT - pipe.GAP) * game_height))
    pipe_bottom_sprite = pygame.transform.scale(pipe_bottom_sprite, (pipe.WIDTH * width, (1 - pipe.MIN_HEIGHT - pipe.GAP) * game_height))

    #prepare the floor
    floor_sprite = pygame.image.load('resources/floor.bmp')
    floor_sprite = pygame.transform.scale(floor_sprite, (width, floor_height))
    floor_rect = floor_sprite.get_rect(topleft=(0,game_height))

    while running:

        #stops from pressing twice in one frame
        key_pressed = False
        move = 0

        for event in pygame.event.get():
            #so can quit
            if event.type == pygame.QUIT: 
                running = False
                break
            
            #jump
            if event.type == pygame.KEYDOWN:
                if key_pressed == False and event.key == pygame.K_SPACE:
                    key_pressed = True
                    move = 1

        #move the bird
        bird.move(move)

        #check if dead
        if bird.is_dead:
            bird.start_state()

        #fill the screen to wipe last frame
        screen.fill((52,225,235))
        
        #draw the pipes
        for item in bird.pipes.items:
            pipe_top_rect = pipe_top_sprite.get_rect(bottomleft=(item.position * width, item.height * game_height))
            pipe_bottom_rect = pipe_bottom_sprite.get_rect(topleft=(item.position * width, item.bottom_height * game_height))
            screen.blit(pipe_top_sprite, pipe_top_rect)
            screen.blit(pipe_bottom_sprite, pipe_bottom_rect)

        #draw the bird
        bird_sprite_rotated = pygame.transform.rotate(bird_sprites[next(bird_sprite_numbers)], bird.angle)
        bird_sprite_rect = bird_sprite_rotated.get_rect(center=(bird.x * width, bird.position * game_height))
        screen.blit(bird_sprite_rotated, bird_sprite_rect)

        #draw the floor
        screen.blit(floor_sprite, floor_rect)

        #show the score
        score = font.render(f'{bird.score}', True, 'white')
        score_rect = score.get_rect(center=(width/2, 0.05 * game_height))
        screen.blit(score, score_rect)

        #display the changes
        pygame.display.flip()

        #advance frame
        dt = clock.tick(60) / 1000

    pygame.quit()