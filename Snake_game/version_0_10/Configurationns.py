from random import choice


class Configurations:
    """
    Clase que contiene todas las configuraciones
    del juego.
    Encapsulamiento: solo getter
    """

    # Configuraciones de pantalla.
    _screen_size = (1280, 720)               # Resolucion pantalla (ancho, alto)
    _game_title = "Snake game de Betho Betho"
    #_background = (28, 30, 50)               # Fondo de pantalla en rgb de 0 a 255
    _fps = 8
    _game_over_screen_time = 3
    #Cinfiguraciones de serpiente:
    _snake_block_size = 80                   #Tamaño del bloque de serpiente
    _snake_head_color = (180, 1, 1)          #Color de la cabeza
    _snake_body_color = (78, 23, 9)          #color de cuerpo

    #Configuraciones para manzana:
    _apple_block_size = 80
    #_apple_block_color = (50, 76, 89)

    #Rutas de archivos multimedia
    _background_image_path = "../media/background_image.jpg"
    _apple_image_path = ["../Media/apple1.png",
                         "../Media/apple2.png",
                         "../Media/apple3.png",]
    _snake_body_image_path =["../Media/body1.png", "../Media/body2.png", "../Media/body3.png"]
    _snake_head_image_path = ["../Media/head1.png", "../Media/head2.png",
                              "../Media/head3.png", "../Media/head4.png",
                              "../Media/head5.png", "../Media/head6.png",
                              "../Media/head7.png", "../Media/head8.png"]

    #Configuracion de animacion:
    _time_to_refresh = 200


    @classmethod
    def get_screen_size (cls) ->tuple[int, int]:
        """
        getter para screen_size
        :return:
        """
        return cls._screen_size
    @classmethod
    def get_game_title(cls)->str:
        """
        getter para game_title
        :return:
        """
        return cls._game_title
    @classmethod
    def get_fps (cls):
        return cls._fps
    @classmethod
    def get_game_over_screen_time (cls):
        return cls._game_over_screen_time
    @classmethod
    def get_snake_block_size (cls):
        """
        getter para el tamaño de serpiente
        :return:
        """
        return cls._snake_block_size
    @classmethod
    def get_snake_head_color(cls):
        return cls._snake_head_color
    @classmethod
    def get_snake_body_color(cls):
        return  cls._snake_body_color
    @classmethod
    def get_apple_block_size(cls):
        return cls._apple_block_size
    @classmethod
    def get_background_image_path(cls)->str:
        """getter para """
        return cls._background_image_path
    @classmethod
    def get_apple_image_path(cls):
        """
        getter para la manzana
        :return:
        """
        return cls._apple_image_path
    @classmethod
    def get_snake_head_image_path (cls):
        return cls._snake_head_image_path
    @classmethod
    def get_snake_body_image_path (cls):
        return cls._snake_body_image_path
    @classmethod
    def get_time_to_refresh(cls):
        return cls._time_to_refresh