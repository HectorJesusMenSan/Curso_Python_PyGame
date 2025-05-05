

import pygame
from Configurationns import  Configurations
from random import randint

class Background:
    """
    Clase que contiene fonfo de pantalla
    """

    def __init__(self):
        background_image_path = Configurations.get_background_image_path()
        self.image = pygame.image.load(background_image_path)
        #Se escala la imagen al tamaño de la pantalla
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)
        self.rect = self.image.get_rect()


    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza pra dibujar el fondo.
        :param screen:
        :return:
        """
        screen.blit(self.image, self.rect)

class Audio:
    def __init__(self):
        #Se carga la musica del juego
        pygame.mixer.music.load("../media/music.mp3")

        #Se cargan los sonidos
        self._start_sound = pygame.mixer.Sound("../media/start_sound.wav")
        self._eats_apple_sound = pygame.mixer.Sound("../media/eats_apple_sound.wav")
        self._game_over_sound = pygame.mixer.Sound("../media/game_over_sound.wav")

    @classmethod
    def play_music(cls, volume)->None:
        pygame.mixer.music.play(loops= -1) #El -1 indica que se reproduce en bucle
        pygame.mixer.music.set_volume(volume)





