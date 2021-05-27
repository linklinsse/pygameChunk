import pygame

class HUD():

    def __init__(self):
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 32)
        self.fps = '0'
        self.fps_text = self.font.render(self.fps, 1, pygame.Color("coral"))

    def update(self, clock):
        self.fps = str(int(clock.get_fps()))
        self.fps_text = self.font.render(self.fps, 1, pygame.Color("coral"))

    def draw(self, surface):
        surface.blit(self.fps_text, (10, 0))