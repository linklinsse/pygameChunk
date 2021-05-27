import pygame

class PossibleAction():

    def __init__(self):
        self.moveVec = pygame.math.Vector2(0, 0)
        self.pickup = False

def notDef(action: PossibleAction):
    print('NotDefinedYet')

def KD_MOVE_UP(action: PossibleAction):
    action.moveVec.y        -= 1

def KD_MOVE_DOWN(action: PossibleAction):
    action.moveVec.y        += 1

def KD_MOVE_LEFT(action: PossibleAction):
    action.moveVec.x        -= 1

def KD_MOVE_RIGHT(action: PossibleAction):
    action.moveVec.x        += 1

def KU_MOVE_UP(action: PossibleAction):
    action.moveVec.y        += 1

def KU_MOVE_DOWN(action: PossibleAction):
    action.moveVec.y        -= 1

def KU_MOVE_LEFT(action: PossibleAction):
    action.moveVec.x        += 1

def KU_MOVE_RIGHT(action: PossibleAction):
    action.moveVec.x        -= 1

def KD_PICKUP(action: PossibleAction):
    action.pickup           = True

KEY_ACTION = {
    pygame.KEYDOWN: {
        pygame.K_UP:    KD_MOVE_UP,
        pygame.K_DOWN:  KD_MOVE_DOWN,
        pygame.K_LEFT:  KD_MOVE_LEFT,
        pygame.K_RIGHT: KD_MOVE_RIGHT,
        pygame.K_SPACE: KD_PICKUP,
    },
    pygame.KEYUP: {
        pygame.K_UP:    KU_MOVE_UP,
        pygame.K_DOWN:  KU_MOVE_DOWN,
        pygame.K_LEFT:  KU_MOVE_LEFT,
        pygame.K_RIGHT: KU_MOVE_RIGHT,
    }
}