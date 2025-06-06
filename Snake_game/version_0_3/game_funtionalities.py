
import pygame


from  Configurationns import Configurations
from  Snake import SnakeBlock

def game_events ( ) -> bool:
    """
    Funcion que administra los eventos del juego
    :return: La bandera del fin del juego

    """

    game_over = False
    # Verificacion de eventos (tecleado, clic y raton) del juego.
    for event in pygame.event.get():
        # Un clic en cerrar juego:
        if event.type == pygame.QUIT:
            game_over = True
     # Retorna bandera
    return  game_over

def screen_refresh(screen: pygame.surface.Surface, clock: pygame.time.Clock, snake_head: SnakeBlock)->None:
    """
    Funcion que administra los elementos visuales.
    :return:
    """
    # Se dibujam elementos graficos en pantalla:
    # Se rellena el objeto pantalla
    screen.fill(Configurations.get_background())


    #Se dibuja la cabeza
    snake_head.blit(screen)

    # Actualizar pantalla
    pygame.display.flip()

    clock.tick(Configurations.get_fps())