import pygame
from pygame.sprite import Sprite
import Configurationns

class Apple(Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.image.fill((50, 76, 89))

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface)->None:
        """
        Se utliza para crear la manzana
        :param screen:
        :return:
        """
        screen.blit(self.image, self.rect)