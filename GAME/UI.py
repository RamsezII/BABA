import os
import pygame

import Codage
    

def getQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


class Screen():
    def __init__(self, etat):
        self.screen = pygame.display.set_mode((720, 480))
        successes, failures = pygame.init()
        print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))
        # pygame.font.init()
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.clock = pygame.time.Clock()

        images_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images")

        pygame.display.set_mode((24*etat.width, 24*etat.height))
        pygame.display.set_icon(pygame.image.load(os.path.join(images_path, "icon.png")))
        pygame.display.set_caption("BABA is A*")

        load_characters = pygame.image.load(os.path.join(images_path, "characters.png")).convert_alpha()
        load_objects = pygame.image.load(os.path.join(images_path, "objects.png")).convert_alpha()
        load_texts = pygame.image.load(os.path.join(images_path, "texts.png")).convert_alpha()
        load_static = pygame.image.load(os.path.join(images_path, "static.png")).convert_alpha()
        load_tiled = pygame.image.load(os.path.join(images_path, "tiled.png")).convert_alpha()

        self.subsurfaces = [
            load_characters.subsurface(1+0*25, 1+0*25, 24, 24),   # BABA
            load_objects.subsurface(426, 1501, 24, 24),   # WALL
            load_static.subsurface(201, 601, 24, 24),   # ROCK
            load_static.subsurface(76, 226, 24, 24),   # FLAG
            load_tiled.subsurface(451, 901, 24, 24),   # LAVA
            load_tiled.subsurface(451, 2348, 24, 24),   # WATER
            load_texts.subsurface(226, 76, 24, 24),   # IS
            load_texts.subsurface(226, 226, 24, 24),   # YOU
            load_texts.subsurface(1, 805, 24, 24),   # SINK
            load_texts.subsurface(226, 1123, 24, 24),   # WIN
            load_texts.subsurface(1, 730, 24, 24),   # DEFEAT
            load_texts.subsurface(1, 301, 24, 24),   # PUSH
            load_texts.subsurface(76, 955, 24, 24),   # SOLID
            load_objects.subsurface(476, 2273, 24, 24),   # wall
            load_tiled.subsurface(476, 901, 24, 24),   # lava
            load_tiled.subsurface(476, 2348, 24, 24),   # water
            load_static.subsurface(226, 601, 24, 24),   # rock
            load_static.subsurface(101, 226, 24, 24),   # flag
            load_characters.subsurface(1+25, 1+0*25, 24, 24),   # baba
        ]


    def deltatime(self, FPS):
        return self.clock.tick(FPS) / 1000


    def refresh(self, etat):
        self.screen.fill(pygame.Color(0, 0, 0))
        for j in range(etat.height):
            j2 = j*etat.width
            for i in range(etat.width):
                for index,flag in etat.grid[j2+i].flags(0, Codage.last_all):
                    if flag != 0:
                        surf = self.subsurfaces[index]
                        if surf:
                            self.screen.blit(surf, (i*24, j*24))
        if etat.win or etat.defeat:
            size = pygame.display.get_window_size()
            surf = pygame.Surface(size)
            surf.set_alpha(125)
            surf.fill(pygame.Color(0,0,0))
            self.screen.blit(surf, (0, 0))
            log = ""
            if etat.win:
                log = "WIN!"
            elif etat.defeat:
                log = "DEFEAT"
            log = self.font.render(log, False, pygame.Color(255,255,255))
            logsize = log.get_size()
            self.screen.blit(log, (0.5*(size[0]-logsize[0]), 0.5*(size[1]-logsize[1])))   
        pygame.display.update()


# if __name__ == "__main__":
#     for x in Flags:
#         print("None,   # " + x.name)
