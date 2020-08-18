from common import *

import os

CAPTION = "Online Fighting Game"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WIDTH = 1600
HEIGHT = 1200
BACK_COLOR = (0, 0, 0)


class Player:
    def __init__(self):
        pass


pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)
CLOCK = pygame.time.Clock()


# Exit the program
def done():
    pygame.quit()
    sys.exit()

running = True
while running:
    SCREEN.fill(BACK_COLOR)
    dt = CLOCK.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done()

    pygame.display.update()

