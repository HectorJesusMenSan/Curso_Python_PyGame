import pygame
from pygame.sprite import Sprite

from Configurations import Configurations
class Soldier(Sprite):
    """Clase del personaje de un soldado"""
    def __init__(self, screen):
        super().__init__()
        soldier_image_path = Configurations.get_soldier_image_path()
        self.image = pygame.image.load(soldier_image_path)

        #Se escala la imagen al tamaño del soldado
        image_soldier_size = Configurations.get_soldier_size()
        self.image = pygame.transform.scale(self.image, image_soldier_size)
        screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.centery = screen_rect.centery
        self.rect.left = screen_rect.left  # Esto colocará el sprite en el borde derecho

        #Logica de movimientos:
        self._is_moving_up = False
        self._is_moving_down = False

        #Velocidad de movimiento
        self._speed = Configurations.get_soldier_speed()
        self._rect_y = float(self.rect.y)


    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza pra dibujar el fondo.
        :param screen:
        :return:
        """
        screen.blit(self.image, self.rect)

    def update_position(self, screen):


        #Actualizar posiciones:
        if self._is_moving_up:
            self._rect_y -= self._speed
        if self._is_moving_down:
            self._rect_y += self._speed

        screen_rect = screen.get_rect()
        if self._rect_y < float(screen_rect.top):
            self._rect_y = float(screen_rect.top)
        elif self._rect_y > float(screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom)
        self.rect.y = self._rect_y

    @property
    def is_moving_up(self):
        return self._is_moving_up
    @is_moving_up.setter
    def is_moving_up(self, valor):
        self._is_moving_up = valor

    @property
    def is_moving_down(self):
        return self._is_moving_down
    @is_moving_down.setter
    def is_moving_down(self, valor):
        self._is_moving_down = valor