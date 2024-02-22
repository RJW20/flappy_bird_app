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
            pygame.draw.rect(screen, 'green', pygame.Rect((width * pipe.position, 0), (width * pipe.width, game_height * pipe.height)))
            pygame.draw.rect(screen, 'green', pygame.Rect((width * pipe.position, (pipe.height + pipe.gap) * game_height), (width * pipe.width, (1 - pipe.height - pipe.gap) * game_height)))

        #draw the bird
        pygame.draw.circle(screen, 'yellow', (width * bird.x, game_height * bird.position), game_height * bird.radius)

        #draw the floor
        pygame.draw.rect(screen, 'brown', pygame.Rect((0, game_height), (width, floor_height)))

        #show the score
        score = font.render(f'{bird.score}', True, 'white')
        score_rect = score.get_rect(center=(width/2, game_height * 0.05))
        screen.blit(score, score_rect)

        #display the changes
        pygame.display.flip()

        #advance frame
        dt = clock.tick(60) / 1000

    pygame.quit()