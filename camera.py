import pygame

class Camera():

    def __init__(self, x = 0, y = 0, zoom = 1):
        self.zoom = zoom
        self.delta = pygame.math.Vector2(x, y)
        self.w, self.h = pygame.display.get_surface().get_size()

    def update(self, x = 0, y = 0, zoom = None):
        if (zoom != None):
            self.zoom = zoom
        self.delta = pygame.math.Vector2(int((x - self.w / (2 * self.zoom)) * self.zoom), int((y - self.h / (2 * self.zoom)) * self.zoom))
