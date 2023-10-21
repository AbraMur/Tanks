import pygame
from constant import *


# класс танка
class Tank(object):
    def __init__(self, screen):
        self.screen = screen
        self.tank_time = 0
        self.tank_sprite = [pygame.image.load('assets/tank/Sprite-0001.png'),
                            pygame.image.load('assets/tank/Sprite-0002.png'),
                            pygame.image.load('assets/tank/Sprite-0003.png'),
                            pygame.image.load('assets/tank/Sprite-0004.png'),
                            pygame.image.load('assets/tank/Sprite-0005.png')]

    def tank_stand(self, center_tank, rotate):
        rotate = rotate * 30
        tank_sprite = pygame.transform.rotate(self.tank_sprite[self.tank_time], rotate)
        self.tank_rect = tank_sprite.get_rect(center=center_tank)
        self.screen.blit(tank_sprite, self.tank_rect)

    def tank_drive(self, center_tank, rotate):
        rotate = rotate * 30
        self.tank_time = (self.tank_time + 1) % 5
        tank_sprite = pygame.transform.rotate(self.tank_sprite[self.tank_time], rotate)
        self.tank_rect = tank_sprite.get_rect(center=center_tank)
        self.screen.blit(tank_sprite, self.tank_rect)
