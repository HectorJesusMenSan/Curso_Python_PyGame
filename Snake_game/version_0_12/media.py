

import pygame
from Configurationns import  Configurations

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
        pygame.mixer.music.load(Configurations.get_music_path())

        #Se cargan los sonidos
        self._start_sound = pygame.mixer.Sound(Configurations.get_start_sound_path())
        self._eats_apple_sound = pygame.mixer.Sound(Configurations.get_eats_apple_sound_path())
        self._game_over_sound = pygame.mixer.Sound(Configurations.get_game_over_sound_path())

    @classmethod
    def play_music(cls, volume)->None:
        """
        Se utiliza para realizar un desvanecimiento de la musica del juego hasta parar
        :param volume: tiempo de desvanecimiento en ms
        :return:
        """
        pygame.mixer.music.play(loops= -1) #El -1 indica que se reproduce en bucle
        pygame.mixer.music.set_volume(volume)


    @classmethod
    def music_fadeout(cls, time):
        """
        Se utiliza para realizar el desvanecimiento de la musica del juego
        :param time:
        :return:
        """
        pygame.mixer.music.fadeout(time)
    def play_start_sound(self)->None:
        """
        Se utiliza para reproduci el sonido cuando epieza el juego
        :return:
        """
        self._start_sound.play()
    def play_eats_sound(self)->None:
        """
        Reproduce sonidos cuando la serpiente come una manzana
        :return:
        """
        self._eats_apple_sound.play()
    def play_game_over(self)->None:
        """Reproduce el sonido cuando pierde el jugador"""
        self._game_over_sound.play()

class Scoreboard:
    def __init__(self):
        self._typeface = "Kimono"
        self._font_size = 40
        self._font_color = (171, 250, 10)

        #Se agrega la imagen con el score
        self._font = pygame.font.SysFont(self._typeface, self._font_size)
        self.image = self._font.render("pontos : 0", True, self._font_color)

        self.rect = self.image.get_rect()
        #Se ajusta la posicion del marcador
        self.rect.x = Configurations.get_screen_size()[0]*0.05
        self.rect.y = Configurations.get_screen_size()[1]*0.05

    def update(self, new_score: int)->None:
        text = "Puntos: " + str(new_score)
        self.image = self._font.render(text, True, self._font_color)
    def blit(self, screen: pygame.surface.Surface ):
        screen.blit(self.image, self.rect)

class GameOverImage:
    def __init__(self):
        self.image = pygame.image.load("../media/game_over_image.png")
        self.rect = self.image.get_rect()
    def blit(self, screen: pygame.surface.Surface):
        #Centrar la imagen en la pantalla
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = screen.get_rect().bottom - Configurations.get_snake_block_size()
        self.blit(self.image, self.rect)







