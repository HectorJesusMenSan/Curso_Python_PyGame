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
        #self.image = pygame.image.load(Configurations.get_apple_image_path()[0])
        apple_block_size = Configurations.get_apple_block_size()

        self._apple_frames = []
        for i in range (len(Configurations.get_apple_image_path())):

            frame = pygame.image.load(Configurations.get_apple_image_path()[i])
            frame = pygame.transform.scale(frame, (apple_block_size, apple_block_size))
            self._apple_frames.append(frame)
        self._last_update_time = pygame.time.get_ticks()
        self._frame_index = 0

        self.image = self._apple_frames[self._frame_index]
        self._frame_index = 1

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

    def animate_apple(self)->None:
        """
        Se utiliza para actualizar el frame visible de la mansana dando
        la impresion de movimiento
        :return:
        """
        current_time = pygame.time.get_ticks()
        time_to_refresh = Configurations.get_time_to_refresh()

        needs_refresh = (current_time - self._last_update_time) >= time_to_refresh

        if needs_refresh:
            self.image = self._apple_frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1
            if self._frame_index >= len(self._apple_frames):
                self._frame_index = 0

    @classmethod
    def get_no_manzanas (cls)->int:
        """
        Gueter para acceder al numero de manzanas
        :return:
        """
        return cls._no_manzanas