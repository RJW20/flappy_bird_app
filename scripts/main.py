from typing import Iterable, Any

import pygame

from flappy_bird_app import Bird


def main() -> None:

    #pygame setup
    width = 480
    game_height = 620
    floor_height = game_height * 0.04
    screen = pygame.display.set_mode((width, game_height + floor_height ))
    pygame.display.set_caption("Flappy Bird")
    pygame.font.init()
    font_height = int(game_height * 0.08)
    font = pygame.font.Font(pygame.font.get_default_font(), font_height)
    clock = pygame.time.Clock()
    running = True
    dt = 0

    #initialise the bird
    bird = Bird()
    bird.start_state()
    bird_sprite = pygame.image.load('resources/bird.bmp')
    bird_sprite = pygame.transform.scale(bird_sprite, (game_height * bird.radius * 8/3, game_height * bird.radius * 2))

    #prepare the pipe
    pipe_body_sprite = pygame.image.load('resources/pipe_body.bmp')

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
        for pipe in bird.pipes.items:
            top_pipe_body = pygame.transform.scale(pipe_body_sprite, (width * pipe.width, game_height * pipe.height))
            bottom_pipe_body = pygame.transform.scale(pipe_body_sprite, (width * pipe.width, (1 - pipe.height - pipe.gap) * game_height))
            top_pipe_rect = top_pipe_body.get_rect(topleft=(width * pipe.position, 0))
            bottom_pipe_rect = bottom_pipe_body.get_rect(topleft=(width * pipe.position, (pipe.height + pipe.gap) * game_height))
            screen.blit(top_pipe_body, top_pipe_rect)
            screen.blit(bottom_pipe_body, bottom_pipe_rect)

        #draw the bird
        bird_sprite_rotated = pygame.transform.rotate(bird_sprite, bird.angle)
        bird_sprite_rect = bird_sprite_rotated.get_rect(center=(width * bird.x, game_height * bird.position))
        screen.blit(bird_sprite_rotated, bird_sprite_rect)

        #draw the floor
        screen.blit(floor_sprite, floor_rect)

        #show the score
        score = font.render(f'{bird.score}', True, 'white')
        score_rect = score.get_rect(center=(width/2, game_height * 0.05))
        screen.blit(score, score_rect)

        #display the changes
        pygame.display.flip()

        #advance frame
        dt = clock.tick(60) / 1000

    pygame.quit()