
import pygame
from pygame.examples.cursors import image
from pygame.sprite import Sprite
from Configurationns import Configurations
from random import  randint


class SnakeBlock(Sprite):
    #Atributos de clase con banderas de movimiento de la serpiente
    _is_moving_right = False
    _is_moving_left = False
    _is_moving_up = False
    _is_moving_down = False

    def __init__(self, is_head: bool = False):
        """
        Constructor de clase
        """
        super().__init__()
        if is_head:
            color = Configurations.get_snake_head_color()
        else:
            color =  Configurations.get_snake_body_color()

        snake_block_size = Configurations.get_snake_block_size()
        #Crear cuadro y darle color
        self.image = pygame.Surface((snake_block_size, snake_block_size))
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

    def snake_head_init(self):
        screen_width = Configurations.get_screen_size()[0]
        screen_height = Configurations.get_screen_size()[1]
        snake_block_size = Configurations.get_snake_block_size()

        self.rect.x = snake_block_size*randint(0, (screen_width//snake_block_size)-1)
        self.rect.y = snake_block_size*randint(0, (screen_height//snake_block_size)-1)


    @classmethod
    def get_is_moving_right(cls)->bool:
        """
        getter para la bandera get_is_moving_right
        :return:
        """
        return  cls._is_moving_right

    @classmethod
    def set_is_moving_right(cls, value) -> None:
        cls._is_moving_right = value


    @classmethod
    def get_is_moving_left(cls)->bool:
        """
        getter para la bandera get_is_moving_right
        :return:
        """
        return  cls._is_moving_left

    @classmethod
    def set_is_moving_left(cls, value) -> None:
        cls._is_moving_left = value

    @classmethod
    def get_is_moving_up(cls) -> bool:
        """
        getter para la bandera get_is_moving_right
        :return:
        """
        return cls._is_moving_up

    @classmethod
    def set_is_moving_up(cls, value) -> None:
        cls._is_moving_up = value

    @classmethod
    def get_is_moving_down(cls) -> bool:
        """
        getter para la bandera get_is_moving_right
        :return:
        """
        return cls._is_moving_down

    @classmethod
    def set_is_moving_down(cls, value) -> None:
        cls._is_moving_down = value
