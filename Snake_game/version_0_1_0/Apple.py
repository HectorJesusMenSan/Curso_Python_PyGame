import pygame

from pygame.sprite import Sprite
from random import randint

from Configurationns import Configurations


class Apple(Sprite):
    #Atributo de clase para la puntuacion.
    _no_manzanas = 0
    def __init__(self):
        super().__init__()

        Apple._no_manzanas += 1

        #self.image = pygame.Surface((Configurations.get_apple_block_size(), Configurations.get_snake_block_size()))
        #self.image.fill(Configurations.get_apple_block_color())
        self.image = pygame.image.load(Configurations.get_apple_image_path())
        apple_block_size = Configurations.get_apple_block_size()
        self.image = pygame.transform.scale(self.image, (apple_block_size, apple_block_size))
        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface)->None:
        """
        Se utliza para crear la manzana
        :param screen:
        :return:
        """
        screen.blit(self.image, self.rect)

    def random_psition(self, sake_body: pygame.sprite.Group)->None:
        """
        Se utiliza para inicializar unaa posicion aleatoria de manzana y verifica que no
        se sobrepomga sobre el cuerpo de la serpiente.
        :return:
        """
        repeat = True
        while repeat:
            #se genera posicion aleatorio
            screen_width = Configurations.get_screen_size()[0]
            screen_height = Configurations.get_screen_size()[1]
            apple_block_size = Configurations.get_snake_block_size()

            self.rect.x = apple_block_size * randint(0, (screen_width // apple_block_size) - 1)
            self.rect.y = apple_block_size * randint(0, (screen_height // apple_block_size) - 1)

            #Se verifica que no esta en el cuerpo de serpiente.
            for snake_block in sake_body.sprites():
                if self.rect is snake_block.rect:
                    repeat = True
                    break
                else:
                    repeat = False
    @classmethod
    def get_no_manzanas (cls)->int:
        """
        Gueter para acceder al numero de manzanas
        :return:
        """
        return cls._no_manzanas