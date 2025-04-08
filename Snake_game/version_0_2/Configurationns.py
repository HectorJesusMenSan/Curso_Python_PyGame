class Configurations:
    """
    Clase que contiene todas las configuraciones
    del juego.
    """

    # Configuraciones de pantalla.
    _screen_size = (1280, 720)               # Resolucion pantalla (ancho, alto)
    _game_title = "Snake game de Betho Betho"
    _background = (28, 30, 50)               # Fondo de pantalla en rgb de 0 a 255

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
    def get_background (cls):

        return cls._background