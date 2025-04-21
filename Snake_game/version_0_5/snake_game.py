"""
Nombre:
Fecha:
Descripcion:
Version 0.3:

"""

#Importar modulos para videojuego
import pygame

from Configurationns import Configurations
from Snake_game.version_0_5.game_funtionalities import snake_movement
from game_funtionalities import screen_refresh
from game_funtionalities import  game_events

from Snake import  SnakeBlock
from pygame.sprite import Group


def run_game() -> None:
    """
    Funcion principal del videojuego.
    :return:
    """
    #Inicializar modulo o recursos
    pygame.init()
    #Configuracion de reloj
    clock = pygame.time.Clock()

    #Iniciarlizar pantalla
    screen = pygame.display.set_mode(Configurations.get_screen_size())

    #Configurar titulo de juego.
    pygame.display.set_caption(Configurations.get_game_title())

    #Se crea bloque inicial de serpiente
    snake_head = SnakeBlock(is_head=True)
    snake_head.snake_head_init()

    #Se crea un grupo para almacenar el cuerpo de la serpiente
    snake_body = Group()
    snake_body.add(snake_head)

    #Ciclo principal de juego:
    game_over = False
    while not game_over:
        # Verificacion de eventos (tecleado, clic y raton) del juego.
        game_over = game_events()
        #Se administra el movimiento de la serpiente
        snake_movement(snake_body)
        #Se dibujan los elementos graficos en la pantalla
        screen_refresh(screen, clock, snake_body)
    #Cerrar recursos.
    pygame.quit()

if __name__ == '__main__':
    run_game()