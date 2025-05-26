class Configurations:
    """
    Clase que contiene todas las configuraciones
    del juego.
    Encapsulamiento: solo getter
    """

    # Configuraciones de pantalla.
    _screen_size = (1280, 720)               # Resolucion pantalla (ancho, alto)
    _game_title = "Alien Game de Me'Sant"
    #_background = (12, 55, 65)               # Fondo de pantalla en rgb de 0 a 255
    _soldier_size = (160,160)
    #Fps para correr juego:
    _fps = 8
    _soldier_speed = 10

    #Imagenes de juego
    _background_image_path = "../Media/jungla_image.jpg"
    _soldier_image_path = "../Media/soldier_image.jpg"

    @classmethod
    def get_screen_size (cls) ->tuple[int, int]:
        """
        getter para screen_size: Tamaño de pantalla
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
    def get_background_image_path(cls) -> str:
        """
        Metodo de acceso para retornar imagen de fondo
        :return: imagen de fondo en str
        """
        return cls._background_image_path

    @classmethod
    def get_soldier_image_path(cls) ->str:
        return cls._soldier_image_path

    @classmethod
    def get_soldier_size(cls) ->tuple[int, int]:
        return cls._soldier_size

    @classmethod
    def get_fps(cls):
        return cls._fps

    @classmethod
    def get_soldier_speed(cls):
        return cls._soldier_speed