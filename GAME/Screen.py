import pygame

from Codage import Flags


screen = pygame.display.set_mode((720, 480))
successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))
clock = pygame.time.Clock()
FPS = 20
setdirty = True


load_characters = pygame.image.load("./images/raw/PC Computer - Baba Is You - Objects Character - ALPHA.png").convert_alpha()
load_objs = pygame.image.load("./images/raw/PC Computer - Baba Is You - Objects Tiled - ALPHA.png").convert_alpha()

baba_word = load_characters.subsurface(1, 1, 24, 24)
baba_obj = load_characters.subsurface(1+25, 1, 24, 24)

wall_obj = load_objs.subsurface(476, 2273, 24, 24)


def vsync():
    return clock.tick(FPS) / 1000


def refresh(etat):
    screen.fill((0, 0, 0))
    for j in range(etat.h):
        for i in range(etat.w):
            flags = etat.grid[j][i]
            pos = (i*24, j*24)
            if flags.hasflags(Flags.wall):
                screen.blit(wall_obj, pos)
            if flags.hasflags(Flags.baba):
                screen.blit(baba_obj, pos)
    pygame.display.update()