"""
Nombre:
Fecha:
Descripcion: Se agrega la manzana

Version 0.7:

"""

#Importar modulos para videojuego
import pygame

from Configurationns import Configurations
from Apple import Apple
from game_funtionalities import snake_movement
from game_funtionalities import screen_refresh
from game_funtionalities import  game_events
import game_funtionalities

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

    #Se crea la manzana:
    apple = Apple()
    apple.random_psition()
    #Se crea un grupo con manzanas:
    apples = Group()
    apples.add(apple)


    #Ciclo principal de juego:
    game_over = False
    while not game_over:
        # Verificacion de eventos (tecleado, clic y raton) del juego.
        game_over = game_events(snake_body, apples)
        #Se administra el movimiento de la serpiente
        snake_movement(snake_body)
        #Se dibujan los elementos graficos en la pantalla
        screen_refresh(screen, clock, snake_body, apples)
    #Cerrar recursos.
    pygame.quit()

if __name__ == '__main__':
    run_game()