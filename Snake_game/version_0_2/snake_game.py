"""
Nombre:
Fecha:
Descripcion:
Version 0.2:

"""

#Importar modulos para videojuego
import pygame

from Configurationns import Configurations
from game_funtionalities import screen_refresh
from game_funtionalities import  game_events

def run_game() -> None:
    """
    Funcion principal del videojuego.
    :return:
    """
    #Inicializar modulo o recursos
    pygame.init()

    #Iniciarlizar pantalla
    screen = pygame.display.set_mode(Configurations.get_screen_size())

    #Configurar titulo de juego.
    pygame.display.set_caption(Configurations.get_game_title())

    #Ciclo principal de juego:
    game_over = False
    while not game_over:
        # Verificacion de eventos (tecleado, clic y raton) del juego.
        game_over = game_events()
        #Se dibujan los elementos graficos en la pantalla
        screen_refresh(screen)
    #Cerrar recursos.
    pygame.quit()

if __name__ == '__main__':
    run_game()