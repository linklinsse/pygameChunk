import pygame
import random

class Entity(pygame.sprite.Sprite):

    def __init__(
            self,
            pos = pygame.math.Vector2(0, 0),
            size = pygame.math.Vector2(1, 1),
            color = (255, 0, 255)
        ):

        pygame.sprite.Sprite.__init__(self)

        self.size = size
        self.color = color
        self.rect = pygame.Rect(
                pos.x,
                pos.y,
                self.size.x,
                self.size.y
            )

        self.effective_zoom = 1

        self.loadSurface()

    def loadSurface(self):
        self.image = pygame.Surface([self.size.x * self.effective_zoom, self.size.y * self.effective_zoom])
        self.image.fill(self.color)

    def zoomChangement(self, zoom):
        self.image = pygame.transform.scale(self.image, (int(self.size.x * zoom), int(self.size.y * zoom)))
        self.effective_zoom = zoom

    def update(self, entitys):
        pass

    def draw(self, surface, camera):
        if (camera.zoom != self.effective_zoom):
            self.zoomChangement(camera.zoom)

        surface.blit(self.image, ((self.rect.x) * camera.zoom - camera.delta.x, (self.rect.y) * camera.zoom - camera.delta.y))
