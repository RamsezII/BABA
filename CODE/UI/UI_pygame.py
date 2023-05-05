import os
import pygame

from CORE.Data import *


cellSize = 24


def getQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


class Screen():
    def __init__(self, etat):
        successes, failures = pygame.init()
        print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))
        # pygame.font.init()
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.clock = pygame.time.Clock()

        images_path = os.path.abspath((__file__))
        images_path = os.path.dirname(images_path)
        images_path = os.path.dirname(images_path)
        images_path = os.path.dirname(images_path)
        images_path = os.path.join(images_path, "images")

        self.screen = pygame.display.set_mode(((2+cellSize)*etat.w, (2+cellSize)*etat.h))
        pygame.display.set_icon(pygame.image.load(os.path.join(images_path, "icon.png")))
        pygame.display.set_caption("BABA is A*")

        load_characters = pygame.image.load(os.path.join(images_path, "characters.png")).convert_alpha()
        load_objects = pygame.image.load(os.path.join(images_path, "objects.png")).convert_alpha()
        load_texts = pygame.image.load(os.path.join(images_path, "texts.png")).convert_alpha()
        load_static = pygame.image.load(os.path.join(images_path, "static.png")).convert_alpha()
        load_tiled = pygame.image.load(os.path.join(images_path, "tiled.png")).convert_alpha()

        self.subsurfaces = [
            load_characters.subsurface(1+0*25, 1+0*25, cellSize, cellSize),   # BABA
            load_objects.subsurface(426, 1501, cellSize, cellSize),   # WALL
            load_static.subsurface(201, 601, cellSize, cellSize),   # ROCK
            load_static.subsurface(76, 226, cellSize, cellSize),   # FLAG
            load_tiled.subsurface(451, 901, cellSize, cellSize),   # LAVA
            load_tiled.subsurface(451, 2348, cellSize, cellSize),   # WATER
            load_texts.subsurface(226, 76, cellSize, cellSize),   # IS
            load_texts.subsurface(226, 226, cellSize, cellSize),   # YOU
            load_texts.subsurface(1, 805, cellSize, cellSize),   # SINK
            load_texts.subsurface(226, 1123, cellSize, cellSize),   # WIN
            load_texts.subsurface(1, 730, cellSize, cellSize),   # DEFEAT
            load_texts.subsurface(1, 301, cellSize, cellSize),   # PUSH
            load_texts.subsurface(76, 955, cellSize, cellSize),   # SOLID
            load_objects.subsurface(476, 2273, cellSize, cellSize),   # wall
            load_tiled.subsurface(476, 901, cellSize, cellSize),   # lava
            load_tiled.subsurface(476, 2348, cellSize, cellSize),   # water
            load_static.subsurface(226, 601, cellSize, cellSize),   # rock
            load_static.subsurface(101, 226, cellSize, cellSize),   # flag
            load_characters.subsurface(1+25, 1+0*25, cellSize, cellSize),   # baba
        ]


    def deltatime(self, FPS):
        return self.clock.tick(FPS) / 1000


    def refresh(self, etat):
        self.screen.fill(pygame.Color(0, 0, 0))
        for j in range(etat.h):
            j2 = j*etat.w
            for i in range(etat.w):
                for index,flag in etat.grid[j2+i].flags(0, BABAb.last_all):
                    if flag != 0:
                        surf = self.subsurfaces[index]
                        if surf:
                            self.screen.blit(surf, ((i+1)*cellSize, (j+1)*cellSize))
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
