import pygame

from Codage import Flags


if __name__ == "__main__":
    for x in Flags:
        print("None,   # " + x.name)


class Screen():
    def __init__(self):
        self.screen = pygame.display.set_mode((720, 480))
        successes, failures = pygame.init()
        print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))
        self.clock = pygame.time.Clock()

        load_characters = pygame.image.load("./images/characters.png").convert_alpha()
        load_objects = pygame.image.load("./images/objects.png").convert_alpha()
        load_texts = pygame.image.load("./images/texts.png")
        load_static = pygame.image.load("./images/static.png")

        self.subsurfaces = [
            load_characters.subsurface(1+0*25, 1+0*25, 24, 24),   # BABA
            load_objects.subsurface(426, 1501, 24, 24),   # WALL
            None,   # ROCK
            load_static.subsurface(76, 226, 24, 24),   # FLAG
            None,   # LAVA
            None,   # WATER
            load_texts.subsurface(226, 76, 24, 24),   # IS
            load_texts.subsurface(226, 226, 24, 24),   # YOU
            None,   # SINK
            load_texts.subsurface(226, 1123, 24, 24),   # WIN
            None,   # DEFEAT
            None,   # PUSH
            None,   # SOLID
            load_characters.subsurface(1+25, 1+0*25, 24, 24),   # baba
            load_objects.subsurface(476, 2273, 24, 24),   # wall
            None,   # rock
            load_static.subsurface(101, 226, 24, 24),   # flag
            None,   # lava
            None,   # water
        ]

        pygame.display.set_icon(pygame.image.load("./images/icon.png"))
        pygame.display.set_caption("BABA is A*")


    def deltatime(self, FPS):
        return self.clock.tick(FPS) / 1000


    def refresh(self, etat):
        self.screen.fill((0, 0, 0))
        for j in range(etat.h):
            for i in range(etat.w):
                for index in etat.grid[j][i].indexes():
                    surf = self.subsurfaces[index]
                    if surf:
                        self.screen.blit(surf, (i*24, j*24))
        pygame.display.update()