from entity import Entity
from pickup import Pickup
from physique import Physique
from UserInput import PossibleAction
import pygame

class Player(Entity):

    def __init__(self, pos = pygame.math.Vector2(0, 0)):
        Entity.__init__(self, pos = pos, color = (255, 0, 0))
        self.move_vector = pygame.math.Vector2(0, 0)
        self.speed = 1
        self.try_pickup = False

    def input(self, action: PossibleAction):
        self.move_vector += action.moveVec
        self.move_vector.x = max(min(1, self.move_vector.x), -1)
        self.move_vector.y = max(min(1, self.move_vector.y), -1)

        if action.pickup:
            self.try_pickup = True

    def update_mov(self, entitys):

        self.rect.x += self.move_vector.x * self.speed
        for ent in entitys:
            if isinstance(ent, Physique):
                if pygame.sprite.collide_rect(self, ent):
                    if (self.move_vector.x > 0):
                        self.rect.right = ent.rect.left
                    else:
                        self.rect.left = ent.rect.right

        self.rect.y += self.move_vector.y * self.speed
        for ent in entitys:
            if isinstance(ent, Physique):
                if pygame.sprite.collide_rect(self, ent):
                    if (self.move_vector.y > 0):
                        self.rect.bottom = ent.rect.top
                    else:
                        self.rect.top = ent.rect.bottom

    def update(self, entitys):

        self.update_mov(entitys)

        margin_pos = 10
        if self.try_pickup:
            self.try_pickup = False
            for ent in entitys:
                if isinstance(ent, Pickup):
                    if (
                        ent.rect.x >= self.rect.x - margin_pos and
                        ent.rect.y >= self.rect.y - margin_pos and
                        ent.rect.x <= self.rect.x + margin_pos and
                        ent.rect.y <= self.rect.y + margin_pos):
                        entitys.remove(ent)
                        break

    def draw(self, surface, camera):
        super().draw(surface, camera)