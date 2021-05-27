from entity import Entity
import pygame

class Physique(Entity):

    def __init__(self, pos = pygame.math.Vector2(0, 0), size = pygame.math.Vector2(1, 1), color = (102, 0, 0)):
        Entity.__init__(self, pos = pos, color = color, size = size)

    def draw(self, surface, camera):
        super().draw(surface, camera)