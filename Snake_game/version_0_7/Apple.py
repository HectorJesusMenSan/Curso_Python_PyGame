import pygame
from pygame.sprite import Sprite
import Configurationns
from random import randint

from Configurationns import Configurations


class Apple(Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((Configurations.get_apple_block_size(), Configurations.get_snake_block_size()))
        self.image.fill(Configurations.get_apple_block_color())

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface)->None:
        """
        Se utliza para crear la manzana
        :param screen:
        :return:
        """
        screen.blit(self.image, self.rect)

    def random_psition(self)->None:
        """
        Se utiliza para inicializar unaa posicion aleatoria.
        :return:
        """
        screen_width = Configurations.get_screen_size()[0]
        screen_height = Configurations.get_screen_size()[1]
        apple_block_size = Configurations.get_snake_block_size()

        self.rect.x = apple_block_size * randint(0, (screen_width // apple_block_size) - 1)
        self.rect.y = apple_block_size * randint(0, (screen_height // apple_block_size) - 1)
