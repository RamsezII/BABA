import pygame

from Codage import Flags


# print()
# i = 0
# for flag in Flags:
#     print("None,   #", flag.name)
#     i += 1


screen = pygame.display.set_mode((720, 480))
successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))
clock = pygame.time.Clock()
FPS = 20
setdirty = True


load_characters = pygame.image.load("./images/characters.png").convert_alpha()
load_objects = pygame.image.load("./images/objects.png").convert_alpha()
load_texts = pygame.image.load("./images/texts.png")
load_static = pygame.image.load("./images/static.png")

subsurfaces = [
    load_characters.subsurface(1+0*25, 1+0*25, 24, 24),   # BABA
    load_objects.subsurface(426, 1501, 24, 24),   # WALL
    None,   # ROCK
    None,   # FLAG
    None,   # LAVA
    None,   # WATER
    load_texts.subsurface(226, 76, 24, 24),   # IS
    load_texts.subsurface(1, 2894, 24, 24),   # YOU
    None,   # SINK
    None,   # WIN
    None,   # DEFEAT
    load_characters.subsurface(1+25, 1+0*25, 24, 24),   # baba
    load_objects.subsurface(476, 2273, 24, 24),   # wall
    None,   # rock
    None,   # flag
    None,   # lava
    None,   # water
]


def vsync():
    return clock.tick(FPS) / 1000


def refresh(etat):
    screen.fill((0, 0, 0))
    for j in range(etat.h):
        for i in range(etat.w):
            for index in etat.grid[j][i].indexes():
                surf = subsurfaces[index]
                if surf:
                    screen.blit(surf, (i*24, j*24))
    pygame.display.update()