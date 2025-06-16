from random import choice

import pygame
from pygame.sprite import Sprite
"""Movimiento horizontal y movimiento verticacl con banderas, se crea lista de verdadero o falso, se escoge
   Se ocupa posicion en y y x y sus respectivas velocidades. agregar aliens a un grupo"""


class Alien(Sprite):
    def __init__(self, screen: pygame.surface.Surface):
        super().__init__()
        #Banderas de movimiento:
        movement = [True, False]
        self._is_moving_up = choice(movement)
        self._is_moving_down = not self._is_moving_up

