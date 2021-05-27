from entity import Entity
from physique import Physique
import random
import pygame

class v2():

    def __init__(self, start = pygame.math.Vector2(0, 0), end = pygame.math.Vector2(0, 0)):
        self.start = pygame.math.Vector2(start.x, start.y)
        self.end = pygame.math.Vector2(end.x, end.y)

    def __str__(self):
        return 'start: {self.start}, end: {self.end}'.format(self=self)

class Chunk():

    def __init__(self, start = pygame.math.Vector2(0, 0), end = pygame.math.Vector2(0, 0)):
        self.pos = v2(start = start, end = end)
        self.size = end - start
        self.entitys = pygame.sprite.Group()
        self.loaded = False

        self.tile_size = 5
        self.tiles = [[0 for i in range(0, int(self.size.x), self.tile_size)] for i in range(0, int(self.size.y), self.tile_size)]
        self.background = pygame.Surface((50, 50))
        self.background.fill((255, 255, 255))
        self.effective_zoom = 1

    def zoomChangement(self, zoom):
        self.background = pygame.transform.scale(self.background, (int(self.size.x * zoom), int(self.size.y * zoom)))
        self.effective_zoom = zoom

    def load(self, entitys):
        i, j = 0, 0
        for row in self.tiles:
            for tiles in row:
                pygame.draw.rect(self.background, (76, 153, (i + j) * 10),
                    pygame.Rect(
                        self.tile_size * i,
                        self.tile_size * j,
                        self.tile_size,
                        self.tile_size
                    ),
                )
                j += 1
            i += 1
            j = 0

        for i in range(30):
                new = Physique(
                        pos = pygame.math.Vector2(
                                random.randrange(self.pos.start.x, self.pos.end.x),
                                random.randrange(self.pos.start.y, self.pos.end.y)
                            ),
                        size = pygame.math.Vector2(2, 2)
                    )
                self.entitys.add(new)
                entitys.add(new)

        self.loaded = True

    def unload(self, entitys):
        for ent in self.entitys:
            ent.kill()

        self.entitys.empty()
        self.loaded = False

    def update(self, entitys):
        for ent in self.entitys:
            ent.update(entitys)

    def draw(self, surface, camera):

        if (camera.zoom != self.effective_zoom):
            self.zoomChangement(camera.zoom)

        surface.blit(self.background, (
            self.pos.start.x * camera.zoom - camera.delta.x,
            self.pos.start.y * camera.zoom - camera.delta.y
            )
        )

        # for ent in self.entitys:
            # ent.draw(surface, camera)

        # pygame.draw.rect(surface, (0,255,0),
        #     pygame.Rect(
        #         (chunk.pos.start.x - 1) * camera.zoom - camera.delta.x,
        #         (chunk.pos.start.y - 1) * camera.zoom - camera.delta.y,
        #         chunk.size.x * camera.zoom,
        #         chunk.size.y * camera.zoom
        #     ),
        #     2
        # )
