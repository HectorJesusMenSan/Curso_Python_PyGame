
import pygame
from pygame.sprite import Sprite
from Configurationns import Configurations
from random import randint, random, choice


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

            #self.image = pygame.image.load(Configurations.get_snake_head_image_path())
            head_block_size = Configurations.get_snake_block_size()
            self._head_frames = []
            for i in range(len(Configurations.get_snake_head_image_path())):
                frame = pygame.image.load(Configurations.get_snake_head_image_path()[i])
                frame = pygame.transform.scale(frame, (head_block_size, head_block_size))
                self._head_frames.append(frame)

            self._last_update_time = pygame.time.get_ticks()
            self._frame_index = 0

            self.image = self._head_frames[self._frame_index]
            self._frame_index = 1

            self.rect = self.image.get_rect()
        else:

            path = choice(Configurations.get_snake_body_image_path())
            self.image = pygame.image.load(path)

        snake_block_size = Configurations.get_snake_block_size()
        self.image = pygame.transform.scale(self.image, (snake_block_size, snake_block_size))

        #Obtener rectangulo
        self.rect = self.image.get_rect()
    #Metodo de estancia:
    def blit(self, screen: pygame.surface.Surface )->None:
        """
        Se utilixa para dibujar el bloque de serpiente
        :param screen:
        :return:
        """
        angle = 0
        if SnakeBlock.get_is_moving_up():
            angle = 90
        elif SnakeBlock.get_is_moving_left():
            angle = 180
        elif SnakeBlock.get_is_moving_down():
            angle = 270
        image_flip = pygame.transform.rotate(self.image, angle)
        screen.blit(image_flip, self.rect)

    def snake_head_init(self):
        screen_width = Configurations.get_screen_size()[0]
        screen_height = Configurations.get_screen_size()[1]
        snake_block_size = Configurations.get_snake_block_size()

        self.rect.x = snake_block_size*randint(0, (screen_width//snake_block_size)-1)
        self.rect.y = snake_block_size*randint(0, (screen_height//snake_block_size)-1)

    def animate_head(self)->None:
        """
        Se utiliza para actualizar el frame visible de la manzana dando
        la impresion de movimiento
        :return:
        """
        current_time = pygame.time.get_ticks()
        time_to_refresh = Configurations.get_time_to_refresh()

        needs_refresh = (current_time - self._last_update_time) >= time_to_refresh

        if needs_refresh:
            self.image = self._head_frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1
            if self._frame_index >= len(self._head_frames):
                self._frame_index = 0





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
