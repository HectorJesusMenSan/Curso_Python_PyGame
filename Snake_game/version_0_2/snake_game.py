"""
Nombre:
Fecha:
Descripcion:
Version 0.2:

"""

#Importar modulos para videojuego
import pygame

from Snake_game.version_0_2.Configurationns import Configurations


def run_game() -> None:
    """
    Funcion principal del videojuego.
    :return:
    """
    #Inicializar modulo o recursos
    pygame.init()

    #Iniciarlizar pantalla

    #screen_size = (1280, 720)       #Resolucion pantalla (ancho, alto)
    screen = pygame.display.set_mode(Configurations.get_screen_size())
    #screen = pygame.display.set_mode(screen_size)

    #Configurar titulo de juego.
    #game_title = "Snake game de Betho Betho"
    #pygame.display.set_caption(game_title)
    pygame.display.set_caption(Configurations.get_game_title())

    #Ciclo principal de juego:
    game_over = False
    while not game_over:
        #Verificacion de eventos (tecleado, clic y raton) del juego.
        for event in pygame.event.get():
            #Un clic en cerrar juego:
            if event.type == pygame.QUIT:
                game_over = True

        # Se dibujam elementos graficos en pantalla:
        #background = (28, 30, 50)   #Fondo de pantalla en rgb de 0 a 255
        #Se rellena el objeto pantalla
        screen.fill(Configurations.get_background())



        #Actualizar pantalla
        pygame.display.flip()
    #Cerrar recursos.
    pygame.quit()

if __name__ == '__main__':
    run_game()