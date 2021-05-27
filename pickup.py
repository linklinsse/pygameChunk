from entity import Entity
import pygame

class Pickup(Entity):

    def __init__(self, pos = pygame.math.Vector2(0, 0)):
        Entity.__init__(self, pos = pos, color = (51, 255, 255))

    def update(self, entitys):
        pass

    def draw(self, surface, camera):
        super().draw(surface, camera)