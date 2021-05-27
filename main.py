from chunk_map import Chunk_map
from camera import Camera
from player import Player
from pickup import Pickup
from hud import HUD
from UserInput import PossibleAction, KEY_ACTION
import pygame

class main():

    def __init__(self, map_size = 500, chunk_size = 50, screen_size = pygame.math.Vector2(750, 750)):
        pygame.init()
        self.map_size = map_size
        self.chunk_size = chunk_size
        self.screen_size = screen_size
        self.map = Chunk_map(map_size = map_size, chunk_size = chunk_size)

        self.hud = HUD()
        self.players = []
        self.players.append(Player(pygame.math.Vector2(map_size / 2 * chunk_size, map_size / 2 * chunk_size)))

        self.entitys = pygame.sprite.Group()
        self.entitys.add(Pickup(pygame.math.Vector2(map_size / 2 * chunk_size, map_size / 2 * chunk_size)))

        self.running = True
        self.surface = pygame.display.set_mode((int(screen_size.x), int(screen_size.y)))
        self.clock = pygame.time.Clock()
        self.camera = Camera(zoom = 7)

    def update_chunk(self):
        self.map.clear_chunk()

        self.map.load_chunk(self.players[0].rect.x, self.players[0].rect.y, self.entitys, margin_pos=self.chunk_size * 2)

    def update(self):
        self.update_chunk()

        self.hud.update(self.clock)
        self.map.update(self.entitys)

        for ply in self.players:
            ply.update(self.entitys)

        for ent in self.entitys:
            ent.update(self.entitys)

        self.camera.update(self.players[0].rect.x, self.players[0].rect.y)

    def input(self):

        playerAction = PossibleAction()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    if (self.camera.zoom > 1):
                        self.camera.zoom -= 1
                    elif self.camera.zoom > 0.1:
                        self.camera.zoom -= 0.1
                if event.key == pygame.K_i:
                    if (self.camera.zoom < 1):
                        self.camera.zoom += 0.1
                    else:
                        self.camera.zoom += 1

            if event.type in KEY_ACTION.keys():
                if event.key in KEY_ACTION[event.type].keys():
                    KEY_ACTION[event.type][event.key](playerAction)

        self.players[0].input(playerAction)

    def draw(self):

        self.surface.fill((0, 0, 0))

        self.map.draw(self.surface, self.camera)

        for ent in self.entitys:
            ent.draw(self.surface, self.camera)

        for ply in self.players:
            ply.draw(self.surface, self.camera)

        self.hud.draw(self.surface)

        pygame.display.flip()

    def start(self):
        while self.running:
            self.clock.tick(60)
            self.update()
            self.input()
            self.draw()

if __name__ == '__main__':
    a = main()
    a.start()