
import pygame
from pygame.examples.cursors import image
from pygame.sprite import Sprite


class SnakeBlock(Sprite):
    def __init__(self):
        """
        Constructor de clase
        """
        super().__init__()
        #Definir color
        color = (255, 0, 0)
        #Crear cuadro y darle color
        self.image = pygame.Surface((40, 40))
        self.image.fill(color)

        #Obtener rectangulo
        self.rect = self.image.get_rect()
    #Metodo de estancia:
    def blit(self, screen: pygame.surface.Surface )->None:
        """
        Se utilixa para dibujar el bloque de serpiente
        :param screen:
        :return:
        """
        screen.blit(self.image, self.rect)