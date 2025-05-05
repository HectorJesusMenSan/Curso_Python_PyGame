import time

import pygame


from  Configurationns import Configurations
from  Snake import SnakeBlock
from Apple import Apple

from media import Background



def game_events () -> bool:
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
        #Clicks de movimientos
        if event.type == pygame.KEYDOWN:
            #derecha
            if event.key == pygame.K_RIGHT:
                SnakeBlock.set_is_moving_right(True)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)
            #izquierda
            if event.key == pygame.K_LEFT:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(True)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_UP:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(True)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_DOWN:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(True)



     # Retorna bandera
    return  game_over



def snake_movement (snake_body: pygame.sprite.Group)->None:
    """
    Funcion para controlar los movimientos de la serpiente
    :param snake_body:
    :return: None
    """

    body_size = len(snake_body.sprites()) - 1
    for i in range(body_size, 0, -1):
        snake_body.sprites()[i].rect.x = snake_body.sprites()[i-1].rect.x
        snake_body.sprites()[i].rect.y = snake_body.sprites()[i-1].rect.y

    head = snake_body.sprites()[0]

    if SnakeBlock.get_is_moving_right():
        head.rect.x += Configurations.get_snake_block_size()
    elif SnakeBlock.get_is_moving_left():
        head.rect.x -= Configurations.get_snake_block_size()
    elif SnakeBlock.get_is_moving_up():
        head.rect.y -= Configurations.get_snake_block_size()
    elif SnakeBlock.get_is_moving_down():
        head.rect.y += Configurations.get_snake_block_size()

def check_collisions (screen: pygame.surface.Surface, snake_body: pygame.sprite.Group, apples: pygame.sprite.Group)->bool:
    """
    Funcion que revisa las colisiones del juego.
    -Cabeza de serpiente con el cuerpo
    _cabeza de serpiente con el borde de pantalla
    -Cabeza de serpiente con manzana
    :param screen: Pantalla
    :param snake_body: cuerpo de serpiente
    :param apples: Grupo con las manzanas
    :return: bandera de fin de juego
    """
    #Se declara bandera de fin de juego
    game_over = False
    #Se obtiene la cabeza de serpiente
    head = snake_body.sprites()[0]

    #Se revisa la condicion de la cabeza de la serpiente con el borde:
    screen_rect = screen.get_rect()

    if head.rect.right > screen_rect.right :
        game_over = True
    if head.rect.left < screen_rect.left:
        game_over = True
    if head.rect.top < screen_rect.top:
        game_over = True
    if head.rect.bottom > screen_rect.bottom:
        game_over = True

    #Se revisa la condicion de la cabeza con el cuerpo de la serpiente
    head_body_collisions = pygame.sprite.spritecollide(head, snake_body, dokill=False)
    if len(head_body_collisions)>1 :
        game_over = True

    #Se revisa la condicion de la cabeza con la manzana
    head_apple_collisions = pygame.sprite.spritecollide(head, apples, dokill=True)
    if len(head_apple_collisions)>0:
        new_snake_block = SnakeBlock()
        new_snake_block.rect.x = snake_body.sprites()[-1].rect.x
        new_snake_block.rect.y = snake_body.sprites()[-1].rect.y
        snake_body.add(new_snake_block)

        new_apple = Apple()
        new_apple.random_psition(snake_body)
        apples.add(new_apple)


    return game_over





def screen_refresh(screen: pygame.surface.Surface, clock: pygame.time.Clock, snake_body: pygame.sprite.Group, apples: pygame.sprite.Group,
                   background: Background)->None:
    """
    Funcion que administra los elementos visuales.
    :return:
    """

    #Se dibuja el fondo de la pantalla:
    background.blit(screen)

    #Se anima el movimiento de manzana
    apples.sprites()[0].animate_apple()

    snake_body.sprites()[0].animate_head()

    #Se dibuja la manzana
    apples.draw(screen)

    #Se dibuja cuerpo de serpiente
    for snake_block in reversed(snake_body.sprites()):

        snake_block.blit(screen)


    clock.tick(Configurations.get_fps())
    # Actualizar pantalla
    pygame.display.flip()

def game_over_screen():
    """
    Funcion con la parte del fin del juego.
    :return:
    """

    time.sleep(Configurations.get_game_over_screen_time())