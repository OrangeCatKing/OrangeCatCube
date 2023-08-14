import pygame
import sys

FPS = 60  # frames per second, the general speed of the program
WINDOW_WIDTH = 1280  # size of window's width in pixels
WINDOW_HEIGHT = 720  # size of windows' height in pixels
WINDOW_TITLE = 'Orange Cat Cube'  # title that appears in the window title bar

# set up the colors (RGB values)
WHITE = (255, 240, 210)
BLACK = (63, 50, 44)
ORANGE = (255, 162, 63)
PURPLE = (155, 93, 229)
RED = (241, 91, 181)
YELLOW = (254, 228, 64)
BLUE = (0, 187, 249)
CYAN = (0, 245, 212)

SCREEN_BACKGROUND_COLOR = ORANGE
CUBE_COLORS = (PURPLE, RED, YELLOW, BLUE, CYAN)

if __name__ == '__main__':
    # pygame setup
    pygame.init()

    # set up the window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    # run the game loop
    clock = pygame.time.Clock()
    dt = 0

    mouse_pos_x = 0
    mouse_pos_y = 0

    while True:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                mouse_pos_x, mouse_pos_y = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos_x, mouse_pos_y = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos_x, mouse_pos_y = event.pos

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(SCREEN_BACKGROUND_COLOR)

        player_pos = pygame.Vector2(mouse_pos_x, mouse_pos_y)
        pygame.draw.circle(screen, BLACK, player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(FPS) / 1000
